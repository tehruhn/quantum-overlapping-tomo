import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def simple_circuit():
    q = QuantumRegister(4)
    c = ClassicalRegister(4)
    qc = QuantumCircuit(q, c)
    qc.h(q[0])
    qc.cx(q[0], q[1])
    return qc