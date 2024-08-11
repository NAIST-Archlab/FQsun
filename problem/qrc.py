



import qiskit


def qrc_Qsun(num_qubits: int, qiskit_circuit: qiskit.QuantumCircuit):
    """_summary_

    Args:
        num_qubits (int): numbero of qubits
        qiskit_circuit (qiskit.QuantumCircuit): _description_

    Returns:
        _type_: _description_
    """
    from Qsun.Qcircuit import Qubit
    from Qsun.Qgates import RX, RZ, RY, H, S, CNOT
    circuit = Qubit(num_qubits)
    # Map Qiskit gates to ProjectQ gates
    for gate in qiskit_circuit.data:
        if gate[0].name == "h":
            H(circuit, gate[1][0]._index)
        elif gate[0].name == "x":
            S(circuit, gate[1][0]._index)
        elif gate[0].name == "cx":
            CNOT(circuit, gate[1][0]._index, gate[1][1]._index)
        elif gate[0].name == "rx":
            RX(circuit, gate[1][0]._index, gate[0].params[0])
        elif gate[0].name == "ry":
            RY(circuit, gate[1][0]._index, gate[0].params[0])
        elif gate[0].name == "rz":
            RZ(circuit, gate[1][0]._index, gate[0].params[0])
    return circuit.probabilities()

def qrc_ProjectQ(num_qubits: int, qiskit_circuit: qiskit.QuantumCircuit):
    from qiskit import QuantumCircuit
    from projectq import MainEngine
    from projectq.backends import Simulator
    from projectq.ops import H, X, S, CNOT, Measure, Rx, Ry, Rz, All
    import itertools, numpy as np
    eng = MainEngine(backend=Simulator(gate_fusion=True), engine_list=[])
    qubits = eng.allocate_qureg(num_qubits)

    # Map Qiskit gates to ProjectQ gates
    for gate in qiskit_circuit.data:
        if gate[0].name == "h":
            H | qubits[gate[1][0]._index]
        elif gate[0].name == "x":
            S | qubits[gate[1][0]._index]
        elif gate[0].name == "cx":
            CNOT | (qubits[gate[1][0]._index], qubits[gate[1][1]._index])
        elif gate[0].name == "rx":
            angle = gate[0].params[0]
            Rx(angle) | qubits[gate[1][0]._index]
        elif gate[0].name == "ry":
            angle = gate[0].params[0]
            Ry(angle) | qubits[gate[1][0]._index]
        elif gate[0].name == "rz":
            angle = gate[0].params[0]
            Rz(angle) | qubits[gate[1][0]._index]
        elif gate[0].name == "measure":
            Measure | qubits[gate[1][0]._index]

    strings = ["".join(seq) for seq in itertools.product("01", repeat = num_qubits)]
    probs = np.array([eng.backend.get_probability(i, qubits) for i in strings])
    All(Measure) | qubits
    return probs


import pennylane as qml

dev = qml.device('default.qubit')
@qml.qnode(dev)
def qrc_Pennylane( num_qubits: int, qc: qiskit.QuantumCircuit):
    qml.from_qiskit(qc)(wires=range(num_qubits))
    # eturn qml.state()
    return qml.probs(wires=range(num_qubits))