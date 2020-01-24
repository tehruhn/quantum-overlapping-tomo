import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def simple_circuit():
    q = QuantumRegister(4)
    c = ClassicalRegister(4)
    qc = QuantumCircuit(q, c)
    qc.h(q[1])
    qc.cx(q[1], q[2])
    qc.barrier()
    # print(qc)
    # qc.h(q[2])
    # qc.cx(q[2], q[3])
    return qc