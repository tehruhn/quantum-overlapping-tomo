import numpy as np

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