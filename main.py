import qiskit
from qiskit import IBMQ, execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.jobstatus import JobStatus, JOB_FINAL_STATES
from math import log2, ceil
from copy import deepcopy
import time

# custom imports 
from create_ghz_circuit import create_ghz_circuit
from create_qot_circuits import create_qot_circuits
from convert_ibm_returned_result_to_dictionary import convert_ibm_returned_result_to_dictionary

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q-community', group='hackathon', project='tokyo-nov-2019')

list_of_backends = provider.backends()
print('\nYou have access to:')
print(list_of_backends)

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
print("hash_functions:", str(hash_functions))
circuit_list = create_qot_circuits(quantum_circuit, hash_functions, k)

simulator_name = 'ibmq_qasm_simulator'
backend = provider.get_backend(simulator_name)
job = execute(circuit_list, backend=backend)

complete = False
status = job.status()
while not complete:
    if job.status() in JOB_FINAL_STATES:
        complete = True
    else:
        time.sleep(3)
        print("computing...")
print("complete!")        

result = job.result()
result_dict = convert_ibm_returned_result_to_dictionary(result)

print("result_dict:", result_dict)
    
    