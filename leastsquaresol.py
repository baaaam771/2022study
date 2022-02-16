import numpy as np
from numpy.linalg import pinv

A = np.arange(2*3).reshape((2, 3))
b = np.array([11, 38])
x = np.array([2, 3, 4])
# print(np.dot(A, x))
print(np.dot(pinv(A), b))
print(pinv(A))
