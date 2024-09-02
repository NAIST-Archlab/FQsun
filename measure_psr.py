from problem import psr
import numpy as np
import time

cost_funcs = [psr.cost_Qsun, psr.cost_ProjectQ, psr.cost_Qiskit, psr.cost_Pennylane]
packages = ['Qsun', 'ProjectQ', 'Qiskit', 'Pennylane']

print("Type funcs")
j = int(input())
print("Type n")
num_qubit = int(input())
for _ in range(10000):
    params = np.ones((3*num_qubit,))
    diff = psr.psr(cost_funcs[j], params)
