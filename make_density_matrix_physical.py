import numpy as np
import numpy.linalg as np_lin
def make_density_matrix_physical(density_matrix):
    density_matrix = density_matrix / density_matrix.trace()
    
    # part 1
    eigenValues, eigenVectors = np_lin.eig(density_matrix)

    # get indices to elements in descending order
    idx = eigenValues.argsort()[::-1]   
    
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:,idx]
    
    newEigenValues = np.zeros(len(eigenValues), dtype=np.complex_)
    
    # part 2
    i = len(eigenValues)
    a = 0
    
    # part 3
    while ((eigenValues[i-1] + a / i) < 0) and (i > 0):
        newEigenValues[i-1] = 0
        a += eigenValues[i-1]
        i -= 1
        
    # part 4
    for j in range(i):
        newEigenValues[j] = eigenValues[j] + a / i
    
    # part 5
    states = []
    for j in range(len(eigenValues)): 
        states.append(newEigenValues[j] * np.outer(eigenVectors[:,j], eigenVectors[:,j].conjugate()))
        
    physical_density_matrix = np.zeros((len(eigenValues), len(eigenValues)), dtype=np.complex_)
    for state in states:
        physical_density_matrix += state
        
    distance = ((density_matrix - physical_density_matrix) * (density_matrix - physical_density_matrix)).trace()
    #print("Closest Valid Density Matrix Distance:", distance)
    
    return physical_density_matrix