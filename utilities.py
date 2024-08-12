import numpy as np

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