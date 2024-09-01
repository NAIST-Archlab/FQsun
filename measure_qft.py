import numpy as np
import matplotlib.pyplot as plt
from problem import qft

funcs = [qft.qft_Qsun, qft.qft_ProjectQ, qft.qft_Qiskit, qft.qft_Pennylane]
print("Type funcs")
func = int(input())
print("Type n")
i = int(input())
for _ in range(10):
    prob = funcs[func](i)
