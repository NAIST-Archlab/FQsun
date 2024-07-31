import qiskit
import qiskit.quantum_info as qi
import numpy as np
import matplotlib.pyplot as plt
def generate_state(num_qubits):
    matrix = qiskit.quantum_info.random_unitary(2**num_qubits).data
    unitary_matrix = qiskit.quantum_info.Operator(matrix)
    qc = qiskit.QuantumCircuit(num_qubits)
    qc.unitary(unitary_matrix, list(range(0, num_qubits)), label='InputUnita')
    return qi.Statevector.from_instruction(qc).data

num_qubits = 20
num_decimals = 7

fidelitiess = np.zeros((num_qubits, num_decimals))
for num_qubit in range(14, num_qubits):
     
    for num_decimal in range(3, num_decimals):
        fidelities = []
        for num_sample in range(1, 3):
            state = generate_state(num_qubit)
            rounded_state = np.round(state, num_decimal)
            fidelity = np.real(np.conjugate(np.transpose(rounded_state)) @ state)
            fidelities.append(fidelity)
        fidelitiess[num_qubit, num_decimal] = np.mean(fidelities)
        print(f"n: {num_qubit}, n_decimal: {num_decimal}")       
        print(np.mean(fidelities))
    np.savetxt("fidelities.txt", fidelitiess)