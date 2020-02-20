import itertools
import re
from calculate_s import calculate_s

# XXYYZZ
# IXIYIZ
# ALL Z - XIYIZI (WRONG)


def process_dictionary_xx_yy_zz(circuit_name, output):
    dictionary = output[circuit_name]
    list_of_keys = list(dictionary.keys())
    # print(list_of_keys)
    num_qubits = len(list_of_keys[0])
    # print(num_qubits)
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = i[0]
        second = i[1]
        # fix 00 and sum
        zz = []
        s1 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "0":
                zz.append(j)
        for k in zz:
            s1 += dictionary[k]
        # fix 01 and sum 
        zo = []
        s2 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "1":
                zo.append(j)
        for k in zo:
            s2 += dictionary[k]

        # fix 10 and sum
        oz = []
        s3 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "0":
                oz.append(j)
        for k in oz:
            s3 += dictionary[k]

        # fix 11 and sum
        oo = []
        s4 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "1":
                oo.append(j)
        for k in oo:
            s4 += dictionary[k]

        total = (s1 - s2 - s3 + s4)/8192
        # print(s1, s2, s3, s4)
        # print(s1)
        
        ### new method
        bases = []
        qubit_count = len(list_of_keys[0])
        for k in range(qubit_count):
            if k in i:
                bases.append('X')
            else:
                bases.append('I')
        # new method
        total = calculate_s(dictionary, i, bases)
        ###
        
        answer.append(total)

    return answer


def process_dictionary_ix_iy_iz(circuit_name, output):
    dictionary = output[circuit_name]
    list_of_keys = list(dictionary.keys())
    # print(list_of_keys)
    num_qubits = len(list_of_keys[0])
    # print(num_qubits)
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # # find two indices to fix
        # first = i[0]
        # second = i[1]
        # # fix 00 and sum
        # zz = []
        # s1 = 0
        # for j in list_of_keys:
        #     if j[first] == "0" and j[second] == "0":
        #         zz.append(j)
        # for k in zz:
        #     s1 += dictionary[k]
        # # fix 01 and sum 
        # zo = []
        # s2 = 0
        # for j in list_of_keys:
        #     if j[first] == "0" and j[second] == "1":
        #         zo.append(j)
        # for k in zo:
        #     s2 += dictionary[k]

        # # fix 10 and sum
        # oz = []
        # s3 = 0
        # for j in list_of_keys:
        #     if j[first] == "1" and j[second] == "0":
        #         oz.append(j)
        # for k in oz:
        #     s3 += dictionary[k]

        # # fix 11 and sum
        # oo = []
        # s4 = 0
        # for j in list_of_keys:
        #     if j[first] == "1" and j[second] == "1":
        #         oo.append(j)
        # for k in oo:
        #     s4 += dictionary[k]

        # total = (s4 + s2 - s3 - s1)/8192
        # # print(s1, s2, s3, s4)
        first = i[0]
        second = i[1]
        # print(first, second)
        s0 = 0
        zero = []
        for j in list_of_keys:
            if j[second] == "0":
                zero.append(j)
        for k in zero:
            s0 += dictionary[k]

        s1 = 0
        one = []
        for j in list_of_keys:
            if j[second] == "1":
                one.append(j)
        for k in one:
            s1 += dictionary[k]
        total = (s1 - s0)/8192
        
        ### new method
        bases = []
        qubit_count = len(list_of_keys[0])
        for k in range(qubit_count):
            if k in i:
                # is first element
                if k == i[0]:
                    bases.append('I')
                else:
                    bases.append('X')
            else:
                bases.append('I')
        
        total = calculate_s(dictionary, i, bases)
        ###
        answer.append(total)

    return answer

def process_dictionary_xi_yi_zi(circuit_name, output):
    dictionary = output[circuit_name]
    list_of_keys = list(dictionary.keys())
    # print(list_of_keys)
    num_qubits = len(list_of_keys[0])
    # print(num_qubits)
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = i[0]
        second = i[1]
        # fix 00 and sum
        zz = []
        s1 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "0":
                zz.append(j)
        for k in zz:
            s1 += dictionary[k]
        # fix 01 and sum 
        zo = []
        s2 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "1":
                zo.append(j)
        for k in zo:
            s2 += dictionary[k]

        # fix 10 and sum
        oz = []
        s3 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "0":
                oz.append(j)
        for k in oz:
            s3 += dictionary[k]

        # fix 11 and sum
        oo = []
        s4 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "1":
                oo.append(j)
        for k in oo:
            s4 += dictionary[k]

        total = (s4 + s3 - s2 - s1)/8192
        # print(s1, s2, s3, s4)
        
        ### new method
        bases = []
        qubit_count = len(list_of_keys[0])
        for k in range(qubit_count):
            if k in i:
                # is first element
                if k == i[1]:
                    bases.append('I')
                else:
                    bases.append('X')
            else:
                bases.append('I')

        total = calculate_s(dictionary, i, bases)
        ###
        
        answer.append(total)

    return answer

def process_dictionary_xy12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = i[0]
        second = i[1]

        # finds hash function that splits differently
        hnum = 0
        for j in range(len(hash_functions)):
            if hash_functions[j][first] != hash_functions[j][second]:
                hnum = j
        circuit_name = str(hnum) + "_0"
        # print(circuit_name)
        dictionary = output[circuit_name]
        list_of_keys = list(dictionary.keys())
        # fix 00 and sum
        zz = []
        s1 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "0":
                zz.append(j)
        for k in zz:
            s1 += dictionary[k]
        # fix 01 and sum 
        zo = []
        s2 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "1":
                zo.append(j)
        for k in zo:
            s2 += dictionary[k]

        # fix 10 and sum
        oz = []
        s3 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "0":
                oz.append(j)
        for k in oz:
            s3 += dictionary[k]

        # fix 11 and sum
        oo = []
        s4 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "1":
                oo.append(j)
        for k in oo:
            s4 += dictionary[k]

        total = (s4 + s1 - s3 - s2)/8192
        # print(s1, s2, s3, s4)
        
        ### New method
        bases = []
        qubit_count = len(list_of_keys[0])
        for k in range(qubit_count):
            if k in i:
                # is first element
                if k == i[0]:
                    bases.append('X')
                if k == i[1]:
                    bases.append('Y')
            else:
                bases.append('I')

        total = calculate_s(dictionary, i, bases)
        ###
        
        answer.append(total)

    return answer

def process_dictionary_yx12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = i[0]
        second = i[1]

        # finds hash function that splits differently
        hnum = 0
        for j in range(len(hash_functions)):
            if hash_functions[j][first] != hash_functions[j][second]:
                hnum = j
        circuit_name = str(hnum) + "_1"
        # print(circuit_name)
        dictionary = output[circuit_name]
        list_of_keys = list(dictionary.keys())
        # fix 00 and sum
        zz = []
        s1 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "0":
                zz.append(j)
        for k in zz:
            s1 += dictionary[k]
        # fix 01 and sum 
        zo = []
        s2 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "1":
                zo.append(j)
        for k in zo:
            s2 += dictionary[k]

        # fix 10 and sum
        oz = []
        s3 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "0":
                oz.append(j)
        for k in oz:
            s3 += dictionary[k]

        # fix 11 and sum
        oo = []
        s4 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "1":
                oo.append(j)
        for k in oo:
            s4 += dictionary[k]

        total = (s4 + s1 - s3 - s2)/8192
        # print(s1, s2, s3, s4)
        
        ### New Method
        bases = []
        qubit_count = len(list_of_keys[0])
        for k in range(qubit_count):
            if k in i:
                bases.append('X')
            else:
                bases.append('I')
        total = calculate_s(dictionary, i, bases)
        ###
        
        answer.append(total)

    return answer

def process_dictionary_xz12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    # print(list_of_nums)
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        # print(i)
        first = i[0]
        second = i[1]

        # finds hash function that splits differently
        hnum = 0
        for j in range(len(hash_functions)):
            if hash_functions[j][first] != hash_functions[j][second]:
                hnum = j
        circuit_name = str(hnum) + "_2"
        # print(circuit_name)
        dictionary = output[circuit_name]
        # print(dictionary)
        # print(first, second)
        # print(hash_functions[hnum][first], hash_functions[hnum][second])
        # print("this was it")
        # if first==0 and second==1:
        #     print(circuit_name)
        #     print(dictionary)
        # if first==2 and second==3:
        #     print(circuit_name)
        #     print(dictionary)
        list_of_keys = list(dictionary.keys())
        # fix 00 and sum
        zz = []
        s1 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "0":
                zz.append(j)
        for k in zz:
            s1 += dictionary[k]
        # fix 01 and sum 
        zo = []
        s2 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "1":
                zo.append(j)
        for k in zo:
            s2 += dictionary[k]

        # fix 10 and sum
        oz = []
        s3 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "0":
                oz.append(j)
        for k in oz:
            s3 += dictionary[k]

        # fix 11 and sum
        oo = []
        s4 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "1":
                oo.append(j)
        for k in oo:
            s4 += dictionary[k]

        total = (s4 + s1 - s3 - s2)/8192
        # print(s1, s2, s3, s4)
        
        ### New Method
        bases = []
        qubit_count = len(list_of_keys[0])
        for k in range(qubit_count):
            if k in i:
                bases.append('X')
            else:
                bases.append('I')
        total = calculate_s(dictionary, i, bases)
        ###
        
        answer.append(total)

    return answer

def process_dictionary_zx12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = i[0]
        second = i[1]

        # finds hash function that splits differently
        hnum = 0
        for j in range(len(hash_functions)):
            if hash_functions[j][first] != hash_functions[j][second]:
                hnum = j
        circuit_name = str(hnum) + "_3"
        # print(circuit_name)
        dictionary = output[circuit_name]
        list_of_keys = list(dictionary.keys())
        # fix 00 and sum
        zz = []
        s1 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "0":
                zz.append(j)
        for k in zz:
            s1 += dictionary[k]
        # fix 01 and sum 
        zo = []
        s2 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "1":
                zo.append(j)
        for k in zo:
            s2 += dictionary[k]

        # fix 10 and sum
        oz = []
        s3 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "0":
                oz.append(j)
        for k in oz:
            s3 += dictionary[k]

        # fix 11 and sum
        oo = []
        s4 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "1":
                oo.append(j)
        for k in oo:
            s4 += dictionary[k]

        total = (s4 + s1 - s3 - s2)/8192
        # print(s1, s2, s3, s4)
        
        ### New Method
        bases = []
        qubit_count = len(list_of_keys[0])
        for k in range(qubit_count):
            if k in i:
                bases.append('X')
            else:
                bases.append('I')
        total = calculate_s(dictionary, i, bases)
        ###
        
        answer.append(total)

    return answer

def process_dictionary_yz12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = i[0]
        second = i[1]

        # finds hash function that splits differently
        hnum = 0
        for j in range(len(hash_functions)):
            if hash_functions[j][first] != hash_functions[j][second]:
                hnum = j
        circuit_name = str(hnum) + "_4"
        # print(circuit_name)
        dictionary = output[circuit_name]
        # if first ==2 and second ==3:
            # print(dictionary)
        list_of_keys = list(dictionary.keys())
        # fix 00 and sum
        zz = []
        s1 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "0":
                zz.append(j)
        for k in zz:
            s1 += dictionary[k]
        # fix 01 and sum 
        zo = []
        s2 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "1":
                zo.append(j)
        for k in zo:
            s2 += dictionary[k]

        # fix 10 and sum
        oz = []
        s3 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "0":
                oz.append(j)
        for k in oz:
            s3 += dictionary[k]

        # fix 11 and sum
        oo = []
        s4 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "1":
                oo.append(j)
        for k in oo:
            s4 += dictionary[k]

        total = (s4 + s1 - s3 - s2)/8192
        # print(s1, s2, s3, s4)
        
        ### New Method
        bases = []
        qubit_count = len(list_of_keys[0])
        for k in range(qubit_count):
            if k in i:
                bases.append('X')
            else:
                bases.append('I')
        total = calculate_s(dictionary, i, bases)
        ###
        
        answer.append(total)

    return answer

def process_dictionary_zy12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for i in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = i[0]
        second = i[1]

        # finds hash function that splits differently
        hnum = 0
        for j in range(len(hash_functions)):
            if hash_functions[j][first] != hash_functions[j][second]:
                hnum = j
        circuit_name = str(hnum) + "_5"
        # print(circuit_name)
        dictionary = output[circuit_name]
        list_of_keys = list(dictionary.keys())
        # fix 00 and sum
        zz = []
        s1 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "0":
                zz.append(j)
        for k in zz:
            s1 += dictionary[k]
        # fix 01 and sum 
        zo = []
        s2 = 0
        for j in list_of_keys:
            if j[first] == "0" and j[second] == "1":
                zo.append(j)
        for k in zo:
            s2 += dictionary[k]

        # fix 10 and sum
        oz = []
        s3 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "0":
                oz.append(j)
        for k in oz:
            s3 += dictionary[k]

        # fix 11 and sum
        oo = []
        s4 = 0
        for j in list_of_keys:
            if j[first] == "1" and j[second] == "1":
                oo.append(j)
        for k in oo:
            s4 += dictionary[k]

        total = (s4 + s1 - s3 - s2)/8192
        # print(s1, s2, s3, s4)
        
        ### New Method
        bases = []
        for k in range(num_qubits):
            if k in i:
                bases.append('X')
            else:
                bases.append('I')
        total = calculate_s(dictionary, i, bases)
        ###
        
        answer.append(total)

    return answer

