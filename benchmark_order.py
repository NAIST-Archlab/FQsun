import numpy as np
import matplotlib.pyplot as plt
from problem import qrc
import time
import qiskit
instructorss = []
instructors = []
num_qubits = 10
for num_qubits in range(3, 11):
    num_layers = 10
    for _ in range(num_layers):
        for i in range(num_qubits - 1):

            instructors.append(['cx', i, i + 1])
            instructorss.append(instructors.copy())

        instructors.append(['cx', num_qubits - 1, 0])
        instructorss.append(instructors.copy())
        for i in range(num_qubits):
            phase = np.random.rand()

            instructors.append(['rx', phase, i])
            instructorss.append(instructors.copy())
            phase = np.random.rand()

            instructors.append(['ry', phase, i])
            instructorss.append(instructors.copy())      
            phase = np.random.rand()

            instructors.append(['rz', phase, i])
            instructorss.append(instructors.copy())  
                
    num_repeats = 2
    timess = []
    for instructors in instructorss:
        times = []
        for _ in range(num_repeats):
            start = time.time()
            qc = qiskit.QuantumCircuit(num_qubits)
            for instructor in instructors:
                if instructor[0] == 'cx':
                    qc.cx(instructor[1], instructor[2])
                elif instructor[0] == 'rx':
                    qc.rx(instructor[1], instructor[2])
                elif instructor[0] == 'ry':
                    qc.ry(instructor[1], instructor[2])
                elif instructor[0] == 'rz':
                    qc.rz(instructor[1], instructor[2])
            prob = qiskit.quantum_info.Statevector.from_instruction(qc).probabilities()
            end = time.time()
            times.append(end-start)
        timess.append(np.mean(times))

    np.savetxt(f'./time/order/order_qiskit_cad114_{num_qubits}qubit.txt', timess)