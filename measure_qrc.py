from problem import qrc
import numpy as np
import time

funcs = [qrc.qrc_Qsun, qrc.qrc_ProjectQ, qrc.qrc_Qiskit, qrc.qrc_Pennylane]
packages = ['Qsun', 'ProjectQ', 'Qiskit', 'Pennylane']

print("Type funcs")
j = int(input())
print("Type n")
num_qubit = int(input())
for _ in range(10000):
    prob = funcs[j](num_qubit, 10)

