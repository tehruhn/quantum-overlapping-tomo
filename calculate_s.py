def calculate_s(data_counts, qubit_indices, pauli_bases):
    number_of_data_points = 0
    s = 0
    
    print("qubit_indices", qubit_indices)
    #print("pauli_bases", pauli_bases)
    #print("data_counts", data_counts.items())
    
    # loop through indices and read measurments
    for key, value in data_counts.items():
        number_of_data_points += value
        number_of_1s = 0
        for i in range(len(qubit_indices)):
            # indexing a string ordered from left qubit to right
            if key[qubit_indices[i]] == "1":
                if pauli_bases[qubit_indices[i]] != 'I':
                    # when not Identity basis
                    number_of_1s += 1
        
        if number_of_1s % 2 == 1:
            # odd number of 1s
            s -= value
        else:
            # even number of 1s
            s += value
    
    # turn counts into probabilities
    final_s = s / number_of_data_points
    
    return final_s