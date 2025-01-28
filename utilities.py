import numpy as np


def fidelity(state1: np.ndarray, state2: np.ndarray):
    state1 = np.expand_dims(state1, axis=0)
    state2 = np.expand_dims(state2, axis=0)
    return (np.abs(np.inner(np.conjugate(state1), state2))**2)[0][0]


def read_complex_numbers(file_path):
    # Read the contents of the text file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Strip whitespace and convert to float
    values = [float(line.strip()) for line in lines]

    # Pair the values to form complex numbers
    complex_numbers = []
    for i in range(0, len(values), 2):
        real_part = values[i]
        imaginary_part = values[i + 1]
        complex_number = real_part + imaginary_part * 1j
        complex_numbers.append(complex_number)
    return np.array(complex_numbers)            

def qasm_to_qasmgates(qasm):
    import re
    gates = qasm.split('\n')[3:-1]
    qasm_gates = []
    for gate in gates:
        gate = gate[:-1].split(' ')
        # print(gate)
        indices = re.findall(r'\d+', gate[1])
        indices = [int(index) for index in indices]
        matches = re.match(r'([a-z]+)(\(\d+\.\d+\))?', gate[0])
        # Extract the function name and value from the matches
        name = matches.group(1).upper()
        name = name[1:] if name[0] == 'C' else name 
        if matches.group(2) is None:
            param = -999
        else:
            param = float(matches.group(2)[1:-1])
        qasm_gates.append((name, param, indices))
    return qasm_gates
