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
from process_dictionary import process_dictionary_xx_yy_zz, process_dictionary_ix_iy_iz

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

vals_for_all_x_basis = process_dictionary_xx_yy_zz("all_x_basis", result_dict)
print("for all x basis:", vals_for_all_x_basis)
vals_for_all_y_basis = process_dictionary_xx_yy_zz("all_y_basis", result_dict)
print("for all y basis:", vals_for_all_y_basis)
vals_for_all_z_basis = process_dictionary_xx_yy_zz("all_z_basis", result_dict)
print("for all z basis:", vals_for_all_z_basis)

vals_for_all_x_basis1 = process_dictionary_ix_iy_iz("all_x_basis", result_dict)
print("for all x basis:", vals_for_all_x_basis1)
vals_for_all_y_basis1 = process_dictionary_ix_iy_iz("all_y_basis", result_dict)
print("for all y basis:", vals_for_all_y_basis1)
vals_for_all_z_basis1 = process_dictionary_ix_iy_iz("all_z_basis", result_dict)
print("for all z basis:", vals_for_all_z_basis1)
    