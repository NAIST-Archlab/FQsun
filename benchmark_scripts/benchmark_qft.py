import numpy as np
import matplotlib.pyplot as plt
from problem import qft
import time

num_qubits = 17
num_repeat = 10

import constant
import json
# ---- Benchamrking PSR on Qsun ----
timess = np.zeros((len(constant.packages), num_qubits))
funcs = [qft.qft_Qsun, qft.qft_ProjectQ, qft.qft_Qiskit, qft.qft_Pennylane]
for j, package in enumerate(constant.packages):
    print(f'-- Package: {package} --')
    for i in range(3, num_qubits + 1):
        print(f'-- # qubits: {i} --')
        times = []
        for _ in range(num_repeat):
            start = time.time()
            prob = funcs[j](i)
            end = time.time()
            times.append(end-start)
        timess[j][i - 1] = np.mean(times)

data = {}
for j, package in enumerate(constant.packages):
    data[package] = list(timess[j])

with open('./time/qft_cad102.json', 'w') as f:
    json.dump(data, f)