import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.quantum_info.random import random_unitary

def randoms_unitary(n):
    q = QuantumRegister(n)
    c = ClassicalRegister(n)
    quantum_circuit = QuantumCircuit(q, c)
    for i in range(quantum_circuit.n_qubits):
        quantum_circuit.h(i)
    if n%2 == 0:
        # set first layer gates
        for i in range(0, n, 2):
            quantum_circuit.append(random_unitary(4), [i, i+1])
        # set second layer gates
        for i in range(1, n-1, 2):
            quantum_circuit.append(random_unitary(4), [i, i+1])
            
    else:
        # set first layer gates
        for i in range(0, n-1, 2):
            quantum_circuit.append(random_unitary(4), [i, i+1])
        # set second layer gates
        for i in range(1, n, 2):
            quantum_circuit.append(random_unitary(4), [i, i+1])

    return quantum_circuit
