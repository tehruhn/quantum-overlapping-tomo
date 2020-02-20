import itertools
import re
from calculate_s import calculate_s


def get_number_of_measurements(result_dict):
    number_of_data_points = 0
    for key, value in result_dict.items():
        number_of_data_points += value
    return number_of_data_points

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
    for combination in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = combination[0]
        second = combination[1]
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

        total = (s1 - s2 - s3 + s4) / get_number_of_measurements(dictionary)
        # print(s1, s2, s3, s4)
        # print(s1)
        
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
    for combination in itertools.combinations(list_of_nums, 2):
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
        first = combination[0]
        second = combination[1]
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
        total = (s1 - s0) / get_number_of_measurements(dictionary)
        
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
    for combination in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = combination[0]
        second = combination[1]
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

        total = (s4 + s3 - s2 - s1) / get_number_of_measurements(dictionary)
        # print(s1, s2, s3, s4)
        
        answer.append(total)

    return answer

def process_dictionary_xy12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for combination in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = combination[0]
        second = combination[1]

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

        total = (s4 + s1 - s3 - s2) / get_number_of_measurements(dictionary)
        # print(s1, s2, s3, s4)
        
        answer.append(total)

    return answer

def process_dictionary_yx12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for combination in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = combination[0]
        second = combination[1]

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

        total = (s4 + s1 - s3 - s2) / get_number_of_measurements(dictionary)
        # print(s1, s2, s3, s4)
        
        answer.append(total)

    return answer

def process_dictionary_xz12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    # print(list_of_nums)
    answer = []
    for combination in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        # print(i)
        first = combination[0]
        second = combination[1]

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

        total = (s4 + s1 - s3 - s2) / get_number_of_measurements(dictionary)
        # print(s1, s2, s3, s4)
        
        answer.append(total)

    return answer

def process_dictionary_zx12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for combination in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = combination[0]
        second = combination[1]

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

        total = (s4 + s1 - s3 - s2) / get_number_of_measurements(dictionary)
        # print(s1, s2, s3, s4)
        
        answer.append(total)

    return answer

def process_dictionary_yz12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for combination in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = combination[0]
        second = combination[1]

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

        total = (s4 + s1 - s3 - s2) / get_number_of_measurements(dictionary)
        # print(s1, s2, s3, s4)
        
        answer.append(total)

    return answer

def process_dictionary_zy12(num_qubits, output, hash_functions):
    # list of numbers to iterate on
    list_of_nums = list(range(num_qubits))
    answer = []
    for combination in itertools.combinations(list_of_nums, 2):
        # find two indices to fix
        first = combination[0]
        second = combination[1]

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

        total = (s4 + s1 - s3 - s2) / get_number_of_measurements(dictionary)
        # print(s1, s2, s3, s4)
        
        answer.append(total)

    return answer

