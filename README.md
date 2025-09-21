# Static Analysis Tool for Program Verification

This project implements a basic static analysis tool for verifying properties of simple imperative programs, inspired by the work of Aarti Gupta and Zachary Kincaid. The tool analyzes code to detect possible errors and verify invariants.

## Features
- Control flow analysis
- Invariant checking
- Example programs and analysis results

## Academic Relevance

## Enhancements
- Added interprocedural analysis
- Added symbolic execution
- Added loop invariant inference
- Richer assertion language

## Example Usage
1. **Run symbolic execution:**
	```python
	from examples import get_example
	from symbolic import symbolic_execute
	stmts = get_example()
	env = {}
	symbolic_execute(stmts, env)
	```
2. **Interprocedural analysis:**
	```python
	from examples import get_example
	from interprocedural import analyze_program
	programs = {"main": get_example()}
	env = {}
	analyze_program(programs, env)
	```
3. **Infer loop invariants:**
	```python
	from examples import get_example
	from loop_invariants import infer_invariant
	from statements import While
	stmts = get_example()
	for stmt in stmts:
		 if isinstance(stmt, While):
			  print(infer_invariant(stmt))
	```

## References
- Aarti Gupta, "Scalable Verification Techniques"
- Zachary Kincaid, "Program Analysis and Verification"