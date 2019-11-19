import numpy as np

def MatrixGeneratingFunction(x):
    def Sigma(y):
        if y == 1:
            return np.matrix([[0,1],[1,0]])
        elif y == 2:
            return np.matrix([[0,1j],[-1j,0]])
        elif y == 3:
            return np.matrix([[1,0],[0,-1]])
        elif y == 0:
            return np.matrix([[1,0],[0,1]])
        else:
            print("Argument in Sigma(_arg) is wrong.")
            return 0
    r = np.zeros((4,4))
    for i in range(0,4):
        for j in range(0,4):
            r = r + (x.item(i,j) * np.kron(Sigma(i), Sigma(j))/4)
    return r