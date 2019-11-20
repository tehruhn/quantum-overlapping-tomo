# quantum-overlapping-tomo

(For the Qiskit Asia camp 2019)

## Intent

https://arxiv.org/pdf/1908.02754.pdf

Implementation (~1000 lines) of non-trivial algorithm that characterizes entanglement for a variety of quantum states that scales exponentially better than previously known methods. The algorithm is based on a theoretical model that works via quantum tomography of partial density matrices that leverages the theory of perfect hash families for constant time lookups. 


## Deliverables

 1. Beginning of a complete, efficient Quantum Tomography Module in Qiskit (currently works for N qubits and k = 2, 4x4 Density Matrices)
 
 2. Submission of a scientific article
 
 
 ## Work to be done
 
 1. Extending from (n, 2) to (n, k) hash families.
 
 2. Refactoring, modularizing.
 
 3. Cythonizing for awesome speedups.
