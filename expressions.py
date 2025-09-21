# Expression evaluation for Static Analysis Tool
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
        if op == '<=': return eval_expr(left, env) <= eval_expr(right, env)
    return None
