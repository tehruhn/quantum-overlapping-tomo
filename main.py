import qiskit
from qiskit import IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from math import log2, ceil
from copy import deepcopy

# custom imports 
from create_ghz_circuit import create_ghz_circuit

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

# print(hash_functions)
def create_qot_circuits(quantum_circuit, hash_functions, k):
    qubit_count = quantum_circuit.n_qubits
    circuit_dict = {}
    qcx = deepcopy(quantum_circuit)
    qcy = deepcopy(quantum_circuit)
    qcz = deepcopy(quantum_circuit)

    # step 1 in the paper

    # measure in x-basis
    for i in range(qubit_count):
        qcx.h(i)
    qcx.measure(range(qubit_count), range(qubit_count))
    # measure in the y-basis
    for i in range(qubit_count):
        qcy.sdg(i)
        qcy.h(i)
    qcy.measure(range(qubit_count), range(qubit_count))
    # measure in the z-basis
    qcz.measure(range(qubit_count), range(qubit_count))

    # step 2 in the paper

    # for each hash function
    for i in range(len(hash_functions)):

        # measurement 1
        m1 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j]:
                m1.sdg(i)
                m1.h(i)
            else:
                m1.h(i)
        m1.measure(range(qubit_count), range(qubit_count))

        # measurement 2
        m2 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j]:
                m2.h(i)
            else:
                m2.sdg(i)
                m2.h(i)
        m2.measure(range(qubit_count), range(qubit_count))

        # measurement 3
        m3 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j] == 0:
                m3.h(i)
        m3.measure(range(qubit_count), range(qubit_count))

        # measurement 4
        m4 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j]:
                m4.h(i)
        m4.measure(range(qubit_count), range(qubit_count))

        # measurement 5
        m5 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j] == 0:
                m5.sdg(i)
                m5.h(i)
        m5.measure(range(qubit_count), range(qubit_count))

        # measurement 6
        m6 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j]:
                m6.sdg(i)
                m6.h(i)
        m6.measure(range(qubit_count), range(qubit_count))
        




    
    