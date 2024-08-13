


packages = ['Qsun', 'ProjectQ', 'Qiskit', 'Pennylane']
line_styles = ['--', '--', '--', '--']
markers = ['o', 'v', 's', 'd']

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
