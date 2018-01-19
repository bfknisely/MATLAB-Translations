"""
Created on Tue Dec 12 21:55:33 2017

@author: Brian

ME311 Lab 08

The purpose of this code is to
a) compute principle stresses, given a stress vector
b) compute natural frequencies and mode shapes for a double pendulum
"""

import numpy as np
from scipy import linalg as la

# Part A: Determine principle stresses based on given stress vector
sigmaIJ = np.matrix('40,20,-18;20,28,12;-18,12,14')  # Stress vector
val, vec = la.eig(sigmaIJ)
print('Part A:')
print('Principle Stresses: | Direction Cosines:')
for n in range(len(val)):
    s = "Sigma %.0f = %.2f ksi | (%.3f, %.3f, %.3f)" % (
        n+1, np.real(val[n]), vec[n, 0], vec[n, 1], vec[n, 2])
    print(s)

# Part B: Determine natural frequencies and mode shapes for double pendulum
print("\nPart B:")
m = 1  # Define pendulum masses
L = 1  # Define pendulum arm lengths
g = 9.8  # Define acceleration of gravity

massMatrix = np.array([(2*m*L, m*L), (m*L, m*L)])
stiffMatrix = np.array([(2*m*g, 0), (0, m*g)])
val2, vec2 = la.eig(stiffMatrix, b=massMatrix)
s1 = "Eigenvalues: %.4f, %.4f" % (np.real(val2[0]), np.real(val2[1]))
s2 = "Eigenvectors:"
print(s1+'\n'+s2)
for n in range(len(vec2)):
    s3 = "%.4f %8.4f" % (vec2[n, 0], vec2[n, 1])
    print(s3)
	
# Add a cool comment
print('Hello world')
