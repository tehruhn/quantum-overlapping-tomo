def reshape_vec_to_mat(vec):
    mat = []
    temp_row = []
    temp_row.append(vec[0])
    temp_row.append(vec[1])
    temp_row.append(vec[2])
    temp_row.append(vec[3])
    mat.append(temp_row)

    temp_row = []
    temp_row.append(vec[4])
    temp_row.append(vec[7])
    temp_row.append(vec[10])
    temp_row.append(vec[12])
    mat.append(temp_row)

    temp_row = []
    temp_row.append(vec[5])
    temp_row.append(vec[11])
    temp_row.append(vec[8])
    temp_row.append(vec[14])
    mat.append(temp_row)

    temp_row = []
    temp_row.append(vec[6])
    temp_row.append(vec[13])
    temp_row.append(vec[15])
    temp_row.append(vec[9])
    mat.append(temp_row)

    return mat
