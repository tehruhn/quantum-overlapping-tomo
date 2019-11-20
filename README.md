# quantum-overlapping-tomo

(For the Qiskit Asia camp 2019)

## Description

https://arxiv.org/pdf/1908.02754.pdf

Implementation of an algorithm that characterizes entanglement for a variety of quantum states that scales exponentially better than previously known methods. The algorithm is based on a theoretical model that works via quantum tomography of partial density matrices that leverages the theory of perfect hash families for constant time lookups. 

This was a challenging project that involved deep understanding of recent state-of-the-art results in measurement theory. It involved the development of a large amount of code (~1000 lines) and was written with the idea of generalising the applications and contributing to the Qiskit codebase in mind, leading to neat structuring of datastructures and modular functions. It also implements a class of (n, k)-perfect hash families, for k = 2, which can be extended to all k < (qubit count). The functions were used to compute all n-Choose-2 density matrices use low-level operations that are readily parallelizable. 

We ran the circuits using the simulator and on all IBM Q physical quantum devices. We obtained results that align with our understanding of these device performances. This project serves as a proof of concept and we hope to apply it to larger numbers of qubits with the hopes that we can exceed the current 20-qubit entanglement found on IBM Q superconducting devices.


## Deliverables

 1. Beginning of a complete, efficient Quantum Tomography Module in Qiskit (currently works for N qubits and k = 2, 4x4 Density Matrices)
 
 2. Submission of a scientific article
 
 
 ## Work to be done
 
 1. Write up and submit as a paper.
 
 2. Refine code and fix bugs to work for all cases.
 
 3. Extending from (n, 2) to (n, k) hash families.
 
 4. Refactoring and modularization for a pull request on qiskit github repo.
 
 5. Cythonizing for awesome speedups.
