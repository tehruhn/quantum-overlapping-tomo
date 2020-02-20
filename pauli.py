import numpy as np

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