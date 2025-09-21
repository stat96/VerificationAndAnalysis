"""
Static Analysis Tool for Program Verification
Analyzes simple imperative programs for control flow and invariants.
"""
from typing import List, Dict, Any

class Statement:
    pass
class Assign(Statement):
    def __init__(self, var: str, expr: Any):
        self.var = var
        self.expr = expr
class If(Statement):
    def __init__(self, cond: Any, then: List[Statement], else_: List[Statement]):
        self.cond = cond
        self.then = then
        self.else_ = else_
class While(Statement):
    def __init__(self, cond: Any, body: List[Statement]):
        self.cond = cond
        self.body = body
class Assert(Statement):
    def __init__(self, cond: Any):
        self.cond = cond

# Simple expression evaluation
def eval_expr(expr, env):
    if isinstance(expr, str):
        return env.get(expr, 0)
    elif isinstance(expr, int):
        return expr
    elif isinstance(expr, tuple):
        op, left, right = expr
        if op == '+': return eval_expr(left, env) + eval_expr(right, env)
        if op == '-': return eval_expr(left, env) - eval_expr(right, env)
        if op == '*': return eval_expr(left, env) * eval_expr(right, env)
        if op == '==': return eval_expr(left, env) == eval_expr(right, env)
        if op == '<': return eval_expr(left, env) < eval_expr(right, env)
        if op == '>': return eval_expr(left, env) > eval_expr(right, env)
    return None

# Control flow analysis and invariant checking
def analyze(statements: List[Statement], env: Dict[str, Any], invariants: List[str]=[]):
    for stmt in statements:
        if isinstance(stmt, Assign):
            env[stmt.var] = eval_expr(stmt.expr, env)
        elif isinstance(stmt, If):
            if eval_expr(stmt.cond, env):
                analyze(stmt.then, env.copy(), invariants)
            else:
                analyze(stmt.else_, env.copy(), invariants)
        elif isinstance(stmt, While):
            while eval_expr(stmt.cond, env):
                analyze(stmt.body, env.copy(), invariants)
        elif isinstance(stmt, Assert):
            result = eval_expr(stmt.cond, env)
            print(f"Assert {stmt.cond}: {'OK' if result else 'FAIL'}")
            if not result:
                print(f"Invariant violated: {stmt.cond}")

# Example program and analysis
def example():
    # x = 0; while x < 5: x = x + 1; assert x <= 5
    stmts = [
        Assign('x', 0),
        While(('<' ,'x', 5), [Assign('x', ('+', 'x', 1))]),
        Assert(('<=', 'x', 5))
    ]
    # Patch for <= operator
    def eval_expr_with_le(expr, env):
        if isinstance(expr, tuple) and expr[0] == '<=':
            return eval_expr_base(expr[1], env) <= eval_expr_base(expr[2], env)
        return eval_expr_base(expr, env)

    # Save original eval_expr
    eval_expr_base = eval_expr
    env = {}
    # Use patched eval_expr in analyze
    def analyze_with_patch(statements, env, invariants=[]):
        for stmt in statements:
            if isinstance(stmt, Assign):
                env[stmt.var] = eval_expr_with_le(stmt.expr, env)
            elif isinstance(stmt, If):
                if eval_expr_with_le(stmt.cond, env):
                    analyze_with_patch(stmt.then, env.copy(), invariants)
                else:
                    analyze_with_patch(stmt.else_, env.copy(), invariants)
            elif isinstance(stmt, While):
                while eval_expr_with_le(stmt.cond, env):
                    analyze_with_patch(stmt.body, env.copy(), invariants)
            elif isinstance(stmt, Assert):
                result = eval_expr_with_le(stmt.cond, env)
                print(f"Assert {stmt.cond}: {'OK' if result else 'FAIL'}")
                if not result:
                    print(f"Invariant violated: {stmt.cond}")
    analyze_with_patch(stmts, env)

if __name__ == "__main__":
    example()
