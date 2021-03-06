from tests.check import check
import z3

# Grover Reversed
check("grover_rev2.slq", "grover_rev", z3.unsat)
check("grover_rev3.slq", "grover_rev", z3.unsat)
check("grover_rev7.slq", "grover_rev", z3.unsat)

# Verification of Grover's Algorithm
# 1 Call
# 2 qubits - uses certainty
check("grover_fixed2.slq", "grover_fixed", z3.unsat)
check("grover_partial3.slq", "grover_partial", z3.unsat)

# 2 Calls
# 3 qubits - problems with measurement/probability
# Likely causing check to be unknown
# Ran for 5 minutes but no sauce
check("grover_err3.slq", "grover_fixed", z3.sat)
check("grover_fixed3.slq", "grover_fixed", z3.unsat)
# 4 qubits
# 5 qubits
# 6 qubits

# 3 Calls - 7-14
# 4 Calls - 15- 24