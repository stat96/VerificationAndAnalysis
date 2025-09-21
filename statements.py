# Statement definitions for Static Analysis Tool
class Statement:
    pass
class Assign(Statement):
    def __init__(self, var: str, expr): self.var = var; self.expr = expr
class If(Statement):
    def __init__(self, cond, then, else_): self.cond = cond; self.then = then; self.else_ = else_
class While(Statement):
    def __init__(self, cond, body): self.cond = cond; self.body = body
class Assert(Statement):
    def __init__(self, cond): self.cond = cond
