# Symbolic execution for Static Analysis Tool
from expressions import eval_expr

def symbolic_execute(stmts, env):
    print("Symbolic execution trace:")
    for stmt in stmts:
        if hasattr(stmt, 'expr'):
            print(f"{stmt}: {eval_expr(stmt.expr, env)}")
        else:
            print(f"{stmt}")
