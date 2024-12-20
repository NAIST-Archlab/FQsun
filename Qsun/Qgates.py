    # -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 21:26:23 2021

@author: ASUS
"""
import numpy as np
import cmath

def H(wavefunction, n):
    """Hadamard gate: math:`\frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-n-1)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i] += amplitude[i]/2**0.5
            new_amplitude[i+cut] += amplitude[i]/2**0.5
        else:
            new_amplitude[i] -= amplitude[i]/2**0.5
            new_amplitude[i-cut] += amplitude[i]/2**0.5  
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([n, 'H'])
    
def X(wavefunction, n):
    """Pauli-X: math:`\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-n-1)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i+cut] += amplitude[i]
        else:
            new_amplitude[i-cut] += amplitude[i]  
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([n, 'X'])
    
def Y(wavefunction, n):
    """Pauli-Y: math:`\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-n-1)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i+cut] += 1.0j*amplitude[i]
        else:
            new_amplitude[i-cut] -= 1.0j*amplitude[i]  
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([n, 'Y'])
    
def Z(wavefunction, n):
    """Pauli-Z: math:`\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i] += amplitude[i]
        else:
            new_amplitude[i] -= amplitude[i]  
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([n, 'Z'])
    
def RX(wavefunction, n, phi=0):
    """PHASE gate: math:`\begin{pmatrix} cos(phi/2) & -sin(phi/2) \\ sin(phi/2) & cos(phi/2) \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-n-1)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i] += cmath.cos(phi/2)*amplitude[i]
            new_amplitude[i+cut] -= 1j*cmath.sin(phi/2)*amplitude[i]
        else:
            new_amplitude[i] += cmath.cos(phi/2)*amplitude[i]
            new_amplitude[i-cut] -= 1j*cmath.sin(phi/2)*amplitude[i] 
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([n, 'RX', '0'])
    
def RY(wavefunction, n, phi=0):
    """PHASE gate: math:`\begin{pmatrix} cos(phi/2) & -sin(phi/2) \\ sin(phi/2) & cos(phi/2) \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-n-1)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i] += cmath.cos(phi/2)*amplitude[i]
            new_amplitude[i+cut] += cmath.sin(phi/2)*amplitude[i]
        else:
            new_amplitude[i] += cmath.cos(phi/2)*amplitude[i]
            new_amplitude[i-cut] -= cmath.sin(phi/2)*amplitude[i] 
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([n, 'RY', '0'])
    
def RZ(wavefunction, n, phi=0):
    """PHASE gate: math:`\begin{pmatrix} 1 & 0 \\ 0 & e^{i \phi} \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i] += cmath.exp(-1j*phi/2)*amplitude[i]
        else:
            new_amplitude[i] += cmath.exp(1j*phi/2)*amplitude[i]  
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([n, 'RZ', '0'])
    
def Phase(wavefunction, n, phi=0):
    """PHASE gate: math:`\begin{pmatrix} 1 & 0 \\ 0 & e^{i \phi} \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i] += amplitude[i]
        else:
            new_amplitude[i] += cmath.exp(1j*phi)*amplitude[i]  
    wavefunction.amplitude = new_amplitude
#     (wavefunction.visual).append([n, 'P', phi])
    
def S(wavefunction, n):
    """Phase(pi/2): math:`\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}`"""
    Phase(wavefunction, n , cmath.pi/2)
    (wavefunction.visual).append([n, 'S'])
    
def T(wavefunction, n):
    """Phase(pi/4): math:`\begin{pmatrix} 1 & 0 \\ 0 & e^{i \pi / 4} \end{pmatrix}`"""
    Phase(wavefunction, n , cmath.pi/4)
    (wavefunction.visual).append([n, 'T'])
    
def Xsquare(wavefunction, n):
    """a square root of the NOT gate."""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-n-1)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        new_amplitude[i] += (1+1j)*amplitude[i]/2
        if states[i][n] == '0':
            new_amplitude[i+cut] += (1-1j)*amplitude[i]/2
        else:
            new_amplitude[i-cut] += (1-1j)*amplitude[i]/2  
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([n, 'XS'])
    
def CNOT(wavefunction, control, target):
    """Flip target if control is |1>: 
    math:`P_0 \otimes I + P_1 \otimes X = \begin{pmatrix} 1&0&0&0 \\ 0&1&0&0 \\
                                            0&0&0&1 \\ 0&0&1&0 \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    if control < target or control > target:
        cut = 2**(qubit_num-target-1)
    else:
        raise TypeError("Control qubit and target qubit must be distinct")
    for i in np.nonzero(amplitude)[0]:
        if states[i][control] == '1':
            if states[i][target] == '0':
                new_amplitude[i+cut] += amplitude[i]
            else:
                new_amplitude[i-cut] += amplitude[i]
        else:
            new_amplitude[i] = amplitude[i]
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([control, target, 'CX'])
    
def CPhase(wavefunction, control, target, phi=0):
    """Controlled PHASE gate: math:`\text{diag}(1, 1, 1, e^{i \phi})`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    if control == target:
        raise TypeError("Control qubit and target qubit must be distinct")
    for i in np.nonzero(amplitude)[0]:
        if states[i][control] == '1':
            if states[i][target] == '0':
                new_amplitude[i] += amplitude[i]
            else:
                new_amplitude[i] += cmath.exp(1j*phi)*amplitude[i] 
        else:
            new_amplitude[i] = amplitude[i]
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([control, target, 'CP', '0'])
    
def CCNOT(wavefunction, control_1, control_2, target):
    """CCNOT - double-controlled-X
    :math:`P_0 \otimes P_0 \otimes I + P_0 \otimes P_1 \otimes I + P_1 \otimes P_0 \otimes I
                                     + P_1 \otimes P_1 \otimes X`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-target-1)
    if control_1 == target or control_2 == target or control_1 == control_2:
        raise TypeError("Control qubit and target qubit must be distinct")
    for i in np.nonzero(amplitude)[0]:
        if states[i][control_1] == '1' and states[i][control_2] == '1':
            if states[i][target] == '0':
                new_amplitude[i+cut] += amplitude[i]
            else:
                new_amplitude[i-cut] += amplitude[i]
        else:
            new_amplitude[i] = amplitude[i]
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([control_1, control_2, target, 'CCX'])
    
def OR(wavefunction, control_1, control_2, target):
    """CCNOT - double-controlled-X
    :math:`P_0 \otimes P_0 \otimes I + P_0 \otimes P_1 \otimes I + P_1 \otimes P_0 \otimes I
                                     + P_1 \otimes P_1 \otimes X`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-target-1)
    if control_1 == target or control_2 == target or control_1 == control_2:
        raise TypeError("Control qubit and target qubit must be distinct")
    for i in np.nonzero(amplitude)[0]:
        if states[i][control_1] == '1' or states[i][control_2] == '1':
            if states[i][target] == '0':
                new_amplitude[i+cut] += amplitude[i]
            else:
                new_amplitude[i-cut] += amplitude[i]
        else:
            new_amplitude[i] = amplitude[i]
    wavefunction.amplitude = new_amplitude
    
def SWAP(wavefunction, target_1, target_2):
    """Swap gate: math:`\begin{pmatrix} 1&0&0&0 \\ 0&0&1&0 \\ 0&1&0&0 \\ 0&0&0&1 \end{pmatrix}`"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    minimum = target_2 ^ ((target_1 ^ target_2) & -(target_1 < target_2))
    maximum = target_1 ^ ((target_1 ^ target_2) & -(target_1 < target_2)) 
    cut = 2**(qubit_num-minimum-1) - 2**(qubit_num-maximum-1)
    if target_1 == target_2:
        raise TypeError("Target qubits must be distinct")
    for i in range(2**qubit_num):
        if states[i][target_1] != states[i][target_2]:
            if int(states[i][maximum]) > int(states[i][minimum]):
#                 print(states[i], 'to', states[i+cut])
                new_amplitude[i+cut] += amplitude[i]                              
            else:
#                 print(states[i], 'to', states[i-cut])
                new_amplitude[i-cut] += amplitude[i]
        else:
#                 print(states[i], 'to', states[i])
            new_amplitude[i] = amplitude[i]
    wavefunction.amplitude = new_amplitude
    (wavefunction.visual).append([target_1, target_2, 'SWAP'])
    
def E(wavefunction, p, n):
    """Quantum depolarizing channel"""
    states = wavefunction.state
    amplitude = wavefunction.amplitude
    qubit_num = len(states[0])
    new_amplitude = np.zeros(2**qubit_num, dtype = np.complex64)
    cut = 2**(qubit_num-n-1)
    if n >= qubit_num or n < 0:
        raise TypeError("Index is out of range")
    for i in np.nonzero(amplitude)[0]:
        if states[i][n] == '0':
            new_amplitude[i+cut] += (p/2)*abs(amplitude[i])**2
            new_amplitude[i] += (1-p/2)*abs(amplitude[i])**2
        else:
            new_amplitude[i-cut] += (p/2)*abs(amplitude[i])**2
            new_amplitude[i] += (1-p/2)*abs(amplitude[i])**2
    #     wavefunction.wave.iloc[0, :] = np.sqrt(new_amplitude)
    for i in range(2**qubit_num):
        if amplitude[i] < 0:
            new_amplitude[i] = - np.sqrt(new_amplitude[i])
        else:
            new_amplitude[i] = np.sqrt(new_amplitude[i])
    wavefunction.amplitude = new_amplitude

def E_all(wavefunction, p_noise, qubit_num):
    if p_noise > 0:
        for i in range(qubit_num):
            E(wavefunction, p_noise, i)