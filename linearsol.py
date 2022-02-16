# Ax=b
# x=A^(-1).b

import numpy as np
from numpy.linalg import inv

# ex1) (2*2)dot(2*2)
# A = np.array([[1, 2], [3, 7]])
# b = np.array([[1, 3], [5, 7]])
# x = np.array([[-3, 7], [2, -2]])
# inv(A) = np.array([[7, -2], [-3, 1]])

# ex2) (2*2) dot 2
# A = np.array([[7, 4], [3, 9]])
# b = np.array([26, 33])
# x = np.array([2, 3])

# ex3) (3*3) dot 3
# A = np.array([[1, 1, 1], [2, 1, 2], [1, 2, 3]])
# b = np.array([9, 15, 20])
# x = np.array([2, 3, 4])

# ex4) (2*2*2) dot 2
# A = np.arange(2*2*2).reshape((2, 2, 2))
# [[[0 1]
#   [2 3]]

#  [[4 5]
#   [6 7]]]
# b = np.array([[3, 13], [23, 33]])
# x = np.array([2, 3])
# print(inv(A))
# print(np.dot(A, x))
# print(np.matmul(inv(A), b))
# print(np.dot(inv(A), b))
# print(inv(A)@b)


# A_inv = inv(A)
# A_inv = np.linalg.inv(A)
# print(A_inv)


# print(np.dot(inv(A), b))
# print(np.dot(A, x))
