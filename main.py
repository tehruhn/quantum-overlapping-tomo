import qiskit
from qiskit import IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from math import log2, ceil

# custom imports 
from create_ghz_circuit import create_ghz_circuit

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q-community', group='hackathon', project='tokyo-nov-2019')

# number of qubits   
n = 4

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

# print(hash_functions)



    
    