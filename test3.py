import qiskit
import qiskit.quantum_info as qi
from qiskit.primitives import Sampler
qc = qiskit.QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
print("State psi: ", qi.Statevector.from_instruction(qc).data)
qc.measure_all()
print(qc.draw())
# sampler = Sampler()
# result = sampler.run(qc, shots = 10000).result().quasi_dists[0]
# print("Measure: ", result)