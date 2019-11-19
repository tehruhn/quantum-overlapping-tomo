import numpy as np
import numpy.linalg as np_lin

def Negativity(x):
#    print(x)
    M = np.zeros(shape=(len(x),len(x)), dtype=np.complex64)
    n = int(np.sqrt(len(x)))
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if (i//n) != (j//n):
                M[n*(j//n) + (i%n), n*(i//n) + (j%n)] = x[i,j]
            else:
                M[i,j] = x[i,j]
#    print(M)
    eigvals = np.linalg.eigvals(M)
#    print(eigvals)
    neg = 0
    for i in range(len(eigvals)):
        if np.real(eigvals[i]) < 0:
            neg = neg - np.real(eigvals[i])
    return neg
    
    
def partial_transpose(matrix, leftside_qubit_count):
    # transpose halfway between two equal halves
    new_matrix = np.zeros(matrix.shape, dtype=np.complex_)
    
    numrows = len(matrix)
    numcols = len(matrix[0])
    
    partition_count = 2 ** leftside_qubit_count
    partition_size = int(round(numrows / partition_count))
    for x1 in range(partition_count):
        for y1 in range(partition_count):
            for x2 in range(partition_size):
                for y2 in range(partition_size):
                    new_matrix[x1*partition_size + y2, y1*partition_size + x2] = matrix[x1*partition_size + x2, y1*partition_size + y2]
    
    return new_matrix
    
def negativity_2(density_matrix):
    rho_partial_transpose = partial_transpose(density_matrix, 1)
    
    eigenValues, eigenVectors = np_lin.eig(rho_partial_transpose)
    
    eigen_sum = 0
    for i in range(len(eigenValues)):
        if eigenValues[i] < 0:
            eigen_sum += eigenValues[i]
        
    return abs(eigen_sum)