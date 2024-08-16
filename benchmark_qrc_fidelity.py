import qiskit
import numpy as np
import time
from problem import psr
import os, utilities
from qoop.core import metric

types = ['FP32', 'FX32', 'FX24']
num_qubits = 17
for datatype in types:
    print(datatype)
    for times in range(1, 101):
        for depth in range(1,11):
            fidelities = []
            for num_qubit in range(3, num_qubits + 1):
                # from sòftware simulator
                origin = np.loadtxt(f'./data/qrc/cpu/{times}/{num_qubit}_{depth}_amplitude.txt')
                # from FPGA emulator
                reconstruct = utilities.read_complex_numbers(f'./data/qrc/FPGA/QRC/{datatype}/Output/{times}/{num_qubit}_{depth}_amplitude.txt')
                fidelities.append(utilities.fidelity(origin, reconstruct))
                save_path = f'./fidelity/qrc/{datatype}/{times}/qrc_{num_qubit}_{depth}_Fidelity.txt'
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
            np.savetxt(save_path, fidelities)