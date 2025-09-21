# Main entry for Static Analysis Tool
from examples import get_example
from analysis import analyze

def main():
    stmts = get_example()
    env = {}
    print("Basic analysis:")
    analyze(stmts, env)
    print("\nSymbolic execution:")
    from symbolic import symbolic_execute
    symbolic_execute(stmts, env)
    print("\nInterprocedural analysis:")
    from interprocedural import analyze_program
    programs = {"main": stmts}
    analyze_program(programs, env)
    print("\nLoop invariant inference:")
    from loop_invariants import infer_invariant
    from statements import While
    for stmt in stmts:
        if isinstance(stmt, While):
            print(infer_invariant(stmt))

if __name__ == "__main__":
    main()
