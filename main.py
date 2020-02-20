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
from simple_circuit import simple_circuit
from simple_graphstate_circuit import simple_graphstate_circuit
from negativity import Negativity, negativity_2
from make_density_matrix_physical import make_density_matrix_physical

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

print("edges:", edges)

#quantum_circuit = simple_circuit()
quantum_circuit = create_graphstate_circuit(edges)
#quantum_circuit = simple_graphstate_circuit()
print(str(quantum_circuit))

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

simulator_name = 'qasm_simulator'
# backend = provider.get_backend(simulator_name)
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

result = job.result()
# print(result.get_counts(circuit_list[0]))
result_dict = convert_ibm_returned_result_to_dictionary(result)
# print(result_dict)

# make new dict with reversed keys
# new_dict = {}
# list_of_keys = list(result_dict.keys())
# for key in list_of_keys:
#   new_dict[key] = {}
#   temp_dict = result_dict[key]
#   l2_of_keys = list(temp_dict.keys())
#   for key2 in l2_of_keys:
#       new_dict[key]["".join(reversed(key2))] = temp_dict[key2]
# print("------")
# print(result_dict)
# print("-----")
# result_dict = new_dict
# print(result_dict)
# print("reversed IBM output")


density_matrix = []
size = (n*(n-1))/2
ones = []
for i in range(int(size)):
    ones.append(1)

# each of these functions return a density matrix for each pair of qubits, 
# thus each return a list of (n*(n-1))/2 elements
density_matrix.append(ones)
density_matrix.append(process_dictionary.process_dictionary_ix_iy_iz("all_x_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_ix_iy_iz("all_y_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_ix_iy_iz("all_z_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_xi_yi_zi("all_x_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_xi_yi_zi("all_y_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_xi_yi_zi("all_z_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_xx_yy_zz("all_x_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_xx_yy_zz("all_y_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_xx_yy_zz("all_z_basis", result_dict))
density_matrix.append(process_dictionary.process_dictionary_xy12(n, result_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_yx12(n, result_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_xz12(n, result_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_zx12(n, result_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_yz12(n, result_dict, hash_functions))
density_matrix.append(process_dictionary.process_dictionary_zy12(n, result_dict, hash_functions))

m = density_matrix
dm = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 

def pauli(s):
    if isinstance(s, str):
        i = 1.j
        Id = np.matrix([[1.0, 0], [0, 1.0]], np.complex_)
        X = np.matrix([[0, 1.0], [1.0, 0]], np.complex_)
        Y = np.matrix([[0, -i], [i, 0]], np.complex_)
        Z = np.matrix([[1, 0], [0, -1]], np.complex_)
        if len(s) == 1:
            if s=="X":
                return X
            elif s=="Y":
                return Y
            elif s=="Z":
                return Z
            else:
                return Id
        else:
            mat = np.matrix([[1.0]], np.complex_)
            for c in s:
                mat = np.kron(mat, pauli(c))
            return mat
    else:
        print("Error: method \"pauli\" only accepts string input for \"s\".")
        
list_of_keys = list(result_dict["all_x_basis"].keys())
num_qubits = len(list_of_keys[0])
list_of_nums = list(range(num_qubits))
combinations = list(itertools.combinations(list_of_nums, 2))
print("combinations:", combinations)
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
    #calculated_density_matrix = make_density_matrix_physical(calculated_density_matrix)
    print(str(combinations[i]) + ":")
    print("negativity:", negativity_2(calculated_density_matrix))
#for mat in desnity_matrix:
#    print(negativity_2(mat))
    
# print(len(dm), len(dm[0]))

# print("XZ")
# print(process_dictionary.process_dictionary_xz12(n, result_dict, hash_functions))
# print("------")
# print(process_dictionary.process_dictionary_xz12(n, result_dict, hash_functions))
# print("------")
# print(process_dictionary.process_dictionary_zx12(n, result_dict, hash_functions))
# print("------")
# print(process_dictionary.process_dictionary_xy12(n, result_dict, hash_functions))
# print("------")
# print(process_dictionary.process_dictionary_yx12(n, result_dict, hash_functions))
# print("------")
# print(process_dictionary.process_dictionary_yz12(n, result_dict, hash_functions))
# print("------")
# print(process_dictionary.process_dictionary_zy12(n, result_dict, hash_functions))
# print("XY")
# print(process_dictionary.process_dictionary_xy12(n, result_dict, hash_functions))
# print(result_dict["all_x_basis"])
# print("------")
# print("XX")
# print(process_dictionary.process_dictionary_xx_yy_zz("all_x_basis", result_dict))
# print("------")
# print()
# print("YY")
# print(process_dictionary.process_dictionary_xx_yy_zz("all_z_basis", result_dict))
# print("------")
# print()
# print("ALL Z BASIS")
# print(process_dictionary.process_dictionary_xx_yy_zz("all_z_basis", result_dict))
# print("------")
# print(result_dict["all_x_basis"])
# print("------")
# print(result_dict["all_y_basis"])
# print("------")
# print(result_dict["all_z_basis"])
# print("------")
# print(result_dict.keys())
# print("--------")
# print(process_dictionary.process_dictionary_ix_iy_iz("all_y_basis", result_dict))
# print("--------")
# print(process_dictionary.process_dictionary_xi_yi_zi("all_x_basis", result_dict))
# print(result_dict["all_x_basis"])
# print("--------")
# print(process_dictionary.process_dictionary_xi_yi_zi("all_z_basis", result_dict))
# print("--------")

# print(process_dictionary.process_dictionary_ix_iy_iz("all_z_basis", result_dict))
# print("--------")
# print(process_dictionary.process_dictionary_xi_yi_zi("all_z_basis", result_dict))
# print("--------")
# print(process_dictionary.process_dictionary_xx_yy_zz("all_z_basis", result_dict))
# print("--------")
# print(process_dictionary.process_dictionary_xz12(n, result_dict, hash_functions))
# print("--------")
#for i in range(len(dm)):
#    print(negativity_2(MatrixGeneratingFunction(np.matrix(reshape_vec_to_mat(dm[i])))))

# print("--------")
# print(MatrixGeneratingFunction(np.matrix(reshape_vec_to_mat(dm[0]))))

# print("--------")
np.set_printoptions(linewidth=np.inf)

# for i in range(len(dm)):
#     mat = MatrixGeneratingFunction(np.matrix(reshape_vec_to_mat(dm[i])))
#     print(mat)
#     print(Negativity(mat))
#     print()

# for i in range(len(dm)):
#   mat = MatrixGeneratingFunction(np.matrix(reshape_vec_to_mat(dm[i])))
#   total = 0;
#   for j in range(mat.shape[0]):
#       for k in range(mat.shape[1]):
#           if j == k:
#               total += mat.item(j,k)
#   print(total)


