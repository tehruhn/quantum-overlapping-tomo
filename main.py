import qiskit
from qiskit import IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from math import log2, ceil
from copy import deepcopy

# custom imports 
from create_ghz_circuit import create_ghz_circuit
from create_qot_circuits import create_qot_circuits

# IBMQ.load_account()
# provider = IBMQ.get_provider(hub='ibm-q-community', group='hackathon', project='tokyo-nov-2019')

# number of qubits   
n = 4
# qubit partition sizes
k = 2

# connections for graph state
edges = []
for i in range(n-1):
    edges.append([i,i+1])

quantum_circuit = create_ghz_circuit(edges)

# global hash function    
hash_functions = []
# here we assume powers of 2
num_func = ceil(log2(n)) 

# populates hash table
for i in range(num_func):
    temp_list = []
    for j in range(n):
        # checks if i'th bit is set in j 
        if j & (1 << i):
            temp_list.append(1)
        else:
            temp_list.append(0)
    hash_functions.append(temp_list)

circuit_list = create_qot_circuits(quantum_circuit, hash_functions, k)

print(circuit_list)


    
    