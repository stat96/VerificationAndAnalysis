# Interprocedural analysis for Static Analysis Tool
from statements import Assign, If, While, Assert
from analysis import analyze

def analyze_program(programs, env):
    for name, stmts in programs.items():
        print(f"Analyzing procedure: {name}")
        analyze(stmts, env)
