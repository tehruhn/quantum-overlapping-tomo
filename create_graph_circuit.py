import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def create_graph_circuit(edges):
    unique_qubits = []
    for edge in edges:
        if edge[0] not in unique_qubits:
            unique_qubits.append(edge[0])
        if edge[1] not in unique_qubits:
            unique_qubits.append(edge[1])
    
    qubit_count = len(unique_qubits)
    
    q = QuantumRegister(qubit_count)
    c = ClassicalRegister(qubit_count)
    quantum_circuit = QuantumCircuit(q, c)    
    
    for qubit in unique_qubits:
        quantum_circuit.h(qubit)
        
    for edge in edges:
        quantum_circuit.h(edge[1])
        quantum_circuit.cx(edge[0], edge[1])
        quantum_circuit.h(edge[1])
        
    return quantum_circuit