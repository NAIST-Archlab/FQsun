import qiskit
import numpy as np
import time
from problem import psr
import os, utilities
from qoop.core import metric

%load_ext autoreload
%autoreload
types = ['FP32', 'FP16', 'FX32', 'FX24', 'FX16']
num_qubits = 17
for datatype in types:
    print(datatype)
    fidelities = []
    for num_qubit in range(3, num_qubits + 1):
        # from sòftware simulator
        state = psr.circuit_Qsun(np.ones(3*num_qubit), num_qubit).amplitude # return amplitudes
        state = np.expand_dims(state, axis=1)
        sigma = state @ np.transpose(np.conjugate(state))
        # from FPGA emulator
        state_psr = utilities.read_complex_numbers(f'./data/psr/FPGA_{datatype}/psr_{datatype}_Output_{num_qubit}_qubit.txt')
        state_psr = np.expand_dims(state_psr, axis=1)
        rho = state_psr @ np.transpose(np.conjugate(state_psr))
        fidelities.append(metric.compilation_trace_fidelity(rho, sigma))
        np.savetxt(f'./fidelity/psr/psr_{datatype}_Fidelity.txt', fidelities)