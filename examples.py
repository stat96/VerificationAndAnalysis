# Example programs for Static Analysis Tool
from statements import Assign, While, Assert

def get_example():
    # x = 0; while x < 5: x = x + 1; assert x <= 5
    stmts = [
        Assign('x', 0),
        While(('<', 'x', 5), [Assign('x', ('+', 'x', 1))]),
        Assert(('<=', 'x', 5))
    ]
    return stmts
