# Richer assertion language for Static Analysis Tool
class Assertion:
    def __init__(self, cond, message=None):
        self.cond = cond
        self.message = message or "Assertion failed"
    def __str__(self):
        return f"assert {self.cond}: {self.message}"
