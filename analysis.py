# Control flow analysis and invariant checking
from statements import Assign, If, While, Assert
from expressions import eval_expr

def analyze(statements, env, invariants=[]):
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
