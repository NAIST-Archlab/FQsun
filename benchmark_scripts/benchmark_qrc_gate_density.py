import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os

num_qubits = 17
for times in range(1, 101):
    for depth in range(1,11):
        num_gates1 = []
        num_gates2 = []
        for num_qubit in range(3, num_qubits + 1):
            # from software simulator
            with open(f'./data/qrc/cpu/{times}/{num_qubit}_{depth}.txt', 'r') as file:
                num_gate1 = 0
                num_gate2 = 0
                for line in file:
                    gate, qubits, angle = eval(line)
                    # Process the gate information here
                    if gate == 'CNOT':
                        num_gate2 += 1
                    else:
                        num_gate1 += 1
                    #print(line)
                num_gates1.append(num_gate1)
                num_gates2.append(num_gate2)
        for i in [1,2]:
            save_path = f'./gate/qrc/{times}/qrc_{depth}depth_NumGate{i}.txt'
            if not os.path.exists(f'./gate/qrc/{times}'):
                os.makedirs(f'./gate/qrc/{times}')
            if i == 1:
                np.savetxt(save_path, num_gates1, fmt='%d')
            else:
                np.savetxt(save_path, num_gates2, fmt='%d')