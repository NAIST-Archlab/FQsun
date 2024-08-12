import itertools
import time
import types
import numpy as np

def circuit_qsun(params: np.ndarray, num_qubits: int):
    """_Generate vanilla ZXZ circuit

    Args:
        params (np.ndarray): parameters for parameterized quantum circuit
        num_qubits (int): number of qubits

    Returns:
        Qsun.Wavefunction.Wavefunction: vanilla quantum circuit
    """
    from Qsun.Qcircuit import Qubit
    from Qsun.Qgates import RX, RZ
    from Qsun.Qwave import Wavefunction

    c: Wavefunction = Qubit(num_qubits)
    for j in range(0, num_qubits):
        RZ(c, j, params[j])
        RX(c, j, params[j + 1])
        RZ(c, j, params[j + 2])
        j += 3
    return c

def cost_qsun(params: np.ndarray) -> float:
    """Just a cost function for benchmarking

    Args:
        params (np.ndarray): parameters

    Returns:
        float: cost value
    """
    c = circuit_qsun(params, len(params)//3)
    prob = c.probabilities()
    return -np.sum([i*prob[i] for i in range(len(prob))])


def psr(cost: types.FunctionType, params: np.ndarray, epsilon: float = np.pi/2, lr: float = 0.01) -> np.ndarray:
    """Return \nabla\mathcal{C}(\theta) by using 2-term parameter shift rule

    Args:
        params (np.ndarray): parameter
        epsilon (float, optional): Shifted value. Defaults to np.pi/2.
        lr (float, optional): learning rate hyperparameter. Defaults to 0.01.

    Returns:
        np.ndarray: gradient of cost function
    """
    grad = np.zeros((3*i,))
    for i in range(len(params)):
        params_1 = params.copy()
        params_2 = params.copy()
        params_1[i] += epsilon
        params_2[i] -= epsilon
        grad[i] = (cost(params_1)-cost(params_2))/(2*np.sin(epsilon))
    for i in range(len(params)):
        params[i] = params[i] - lr*grad[i] # SGD
    return params
