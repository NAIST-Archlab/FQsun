import qiskit
import numpy as np
import time
from problem import qft
import os, utilities
from qoop.core import metric

types = ['FP32', 'FP16', 'FX32', 'FX24', 'FX16']
num_qubits = 17
for datatype in types:
    print(datatype)
    fidelities = []
    for num_qubits in range(3, num_qubits + 1):
        # from software simulator
        state = qft.qft_Qsun_verify(num_qubits) # return amplitudes
        state = np.expand_dims(state, axis=1)
        sigma = state @ np.transpose(np.conjugate(state))
        # from FPGA emulator
        state_qft = utilities.read_complex_numbers(f'./data/qft/FPGA_{datatype}/QFT_{datatype}_Output_{num_qubits}_qubit.txt')
        state_qft = np.expand_dims(state_qft, axis=1)
        rho = state_qft @ np.transpose(np.conjugate(state_qft))
        fidelities.append(metric.compilation_trace_fidelity(rho, sigma))
        np.savetxt(f'./fidelity/qft/psr_{datatype}_Fidelity.txt', fidelities)