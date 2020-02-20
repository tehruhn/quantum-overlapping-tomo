import qiskit
from qiskit import IBMQ, execute, Aer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.jobstatus import JobStatus, JOB_FINAL_STATES
from math import log2, ceil
from copy import deepcopy
import time
import numpy as np
import itertools

# custom imports 
from create_graphstate_circuit import create_graphstate_circuit
from create_qot_circuits import create_qot_circuits
from convert_ibm_returned_result_to_dictionary import convert_ibm_returned_result_to_dictionary
import process_dictionary
from shot_count_from_dict_of_results import shot_count_from_dict_of_results
from shot_count_from_results import shot_count_from_results
from reshape_vec_to_mat import reshape_vec_to_mat
from mgf import MatrixGeneratingFunction
from negativity import Negativity
from create_simple_ghz_circuit import create_simple_ghz_circuit
from create_simple_graphstate_circuit import create_simple_graphstate_circuit
from negativity import Negativity, negativity_2
from make_density_matrix_physical import make_density_matrix_physical
from pauli import pauli

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q-community', group='hackathon', project='tokyo-nov-2019')

list_of_backends = provider.backends()
print('\nYou have access to:')
print(list_of_backends)

# defines the connections in the graph state
edges = []
for i in range(3): # 4 qubits
    edges.append([i,i+1])

print("edges:", edges)

quantum_circuit = create_simple_ghz_circuit()
#quantum_circuit = create_simple_graphstate_circuit()
#quantum_circuit = create_graphstate_circuit(edges)
print(str(quantum_circuit))

# extracting qubit count here so that we don't need to know which create circuit method we called
qubit_count = len(quantum_circuit.qregs[0])

# qubit partition sizes
k = 2

# global hash function    
hash_functions = []
# here we assume powers of 2
num_func = ceil(log2(qubit_count)) 

# populates hash table
for i in range(num_func):
    temp_list = []
    for j in range(qubit_count):
        # checks if i'th bit is set in j 
        if j & (1 << i):
            temp_list.append(1)
        else:
            temp_list.append(0)
    hash_functions.append(temp_list)
print("hash_functions:", str(hash_functions))
circuit_list = create_qot_circuits(quantum_circuit, hash_functions, k)

simulator_name = 'qasm_simulator'
backend = Aer.get_backend(simulator_name)
job = execute(circuit_list, backend=backend, shots=8192)

complete = False
status = job.status()
while not complete:
    if job.status() in JOB_FINAL_STATES:
        complete = True
    else:
        time.sleep(3)
        print("computing...")
print("complete!")        

all_results = job.result()
all_results_dict = convert_ibm_returned_result_to_dictionary(all_results)
    
size = (qubit_count*(qubit_count-1))/2
ones = []
for i in range(int(size)):
    ones.append(1)

density_matrix = []

# each of these functions return a density matrix for each pair of qubits, 
# thus each return a list of (n*(n-1))/2 elements
density_matrix.append(ones)
density_matrix.append(process_dictionary.process_dictionary_ix_iy_iz("all_x_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_ix_iy_iz("all_y_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_ix_iy_iz("all_z_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_xi_yi_zi("all_x_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_xi_yi_zi("all_y_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_xi_yi_zi("all_z_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_xx_yy_zz("all_x_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_xx_yy_zz("all_y_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_xx_yy_zz("all_z_basis", all_results_dict))
density_matrix.append(process_dictionary.process_dictionary_xy12(qubit_count, all_results_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_yx12(qubit_count, all_results_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_xz12(qubit_count, all_results_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_zx12(qubit_count, all_results_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_yz12(qubit_count, all_results_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_zy12(qubit_count, all_results_dict, hash_functions))

# these couple of lines are no longer needed, will keep here in case someone needs it.
#m = density_matrix
#dm = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
    
qubit_numbers = list(range(qubit_count))
# list each possible combination of qubits (without double counting, i.e. if includes (0,1) then does not include (1,0))
combinations = list(itertools.combinations(qubit_numbers, 2))
print("combinations:", combinations)

# construct the reduced density matrix (as shown in Eq. 8 of the Quantum Overlapping Tomography paper)
# note that the equation in the paper is missing a normalisation constant. I think k^-2 is correct but might need to double check.
for i in range(len(combinations)):
    calculated_density_matrix = pauli("II") / pow(k, 2)
    calculated_density_matrix += density_matrix[1][i] * pauli("IX") / pow(k, 2)
    calculated_density_matrix += density_matrix[2][i] * pauli("IY") / pow(k, 2)
    calculated_density_matrix += density_matrix[3][i] * pauli("IZ") / pow(k, 2)
    calculated_density_matrix += density_matrix[4][i] * pauli("XI") / pow(k, 2)
    calculated_density_matrix += density_matrix[5][i] * pauli("YI") / pow(k, 2)
    calculated_density_matrix += density_matrix[6][i] * pauli("ZI") / pow(k, 2)
    calculated_density_matrix += density_matrix[7][i] * pauli("XX") / pow(k, 2)
    calculated_density_matrix += density_matrix[8][i] * pauli("YY") / pow(k, 2)
    calculated_density_matrix += density_matrix[9][i] * pauli("ZZ") / pow(k, 2)
    calculated_density_matrix += density_matrix[10][i] * pauli("XY") / pow(k, 2)
    calculated_density_matrix += density_matrix[11][i] * pauli("YX") / pow(k, 2)
    calculated_density_matrix += density_matrix[12][i] * pauli("XZ") / pow(k, 2)
    calculated_density_matrix += density_matrix[13][i] * pauli("ZX") / pow(k, 2)
    calculated_density_matrix += density_matrix[14][i] * pauli("YZ") / pow(k, 2)
    calculated_density_matrix += density_matrix[15][i] * pauli("ZY") / pow(k, 2)
    calculated_density_matrix = make_density_matrix_physical(calculated_density_matrix)
    print(str(combinations[i]) + ":")
    print("negativity:", Negativity(calculated_density_matrix))

np.set_printoptions(linewidth=np.inf)


