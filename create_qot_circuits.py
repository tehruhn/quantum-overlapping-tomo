import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from copy import deepcopy


def create_qot_circuits(quantum_circuit, hash_functions, k=2):
    qubit_count = quantum_circuit.n_qubits
    qcx = deepcopy(quantum_circuit)
    qcx.name = "all_x_basis"
    qcy = deepcopy(quantum_circuit)
    qcy.name = "all_y_basis"
    qcz = deepcopy(quantum_circuit)
    qcz.name = "all_z_basis"

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

    name = ""
    circuit_list = []
    circuit_list.append(qcx)
    circuit_list.append(qcy)
    circuit_list.append(qcz)

    # for each hash function
    # naming convention
    # hashfnnumber_measrurementnber
    for i in range(len(hash_functions)):
        temp_list = []
        thisname = name + str(i) + "_"
        # measurement 1
        m1 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j]:
                m1.sdg(i)
                m1.h(i)
            else:
                m1.h(i)
        m1.measure(range(qubit_count), range(qubit_count))
        m1.name = thisname + "0"

        # measurement 2
        m2 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j]:
                m2.h(i)
            else:
                m2.sdg(i)
                m2.h(i)
        m2.measure(range(qubit_count), range(qubit_count))
        m2.name = thisname + "1"

        # measurement 3
        m3 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j] == 0:
                m3.h(i)
        m3.measure(range(qubit_count), range(qubit_count))
        m3.name = thisname + "2"

        # measurement 4
        m4 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j]:
                m4.h(i)
        m4.measure(range(qubit_count), range(qubit_count))
        m4.name = thisname + "3"

        # measurement 5
        m5 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j] == 0:
                m5.sdg(i)
                m5.h(i)
        m5.measure(range(qubit_count), range(qubit_count))
        m5.name = thisname + "4"

        # measurement 6
        m6 = deepcopy(quantum_circuit)
        for j in range(qubit_count):
            if hash_functions[i][j]:
                m6.sdg(i)
                m6.h(i)
        m6.measure(range(qubit_count), range(qubit_count))
        m6.name = thisname + "5"

        circuit_list.append(m1)
        circuit_list.append(m2)
        circuit_list.append(m3)
        circuit_list.append(m4)
        circuit_list.append(m5)
        circuit_list.append(m6)

    return circuit_list
