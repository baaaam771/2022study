import numpy as np

# A = np.array([[1, 2, 3], [4, 5, 6]])
# R = np.einsum("ij->ji", A)
# print(R)


# A = np.eye(10)
# print(A)
# diag = np.einsum('ii->i', A)
# trace = np.einsum('ii->', A)
# print(diag)
# print(trace)

# A = np.array([[1, 2, 3], [4, 5, 6]])
# R = np.einsum("ij->", A)
# print(A)
# print(R)

# x = np.array([1, 2, 3])
# y = np.array([7, 8, 9])
# dot = np.einsum('i,i->', x, y)
# outer = np.einsum('i,j->ij', x, y)
# print(dot)
# print(outer)


# x = np.array([-1, -10, -100])
# y = np.array([1, 10, 100])
# elemwise_vec = np.einsum('i,i->i', x, y)
# print(elemwise_vec)
# A = np.arange(6).reshape((2, 3))
# B = np.arange(6).reshape((2, 3))
# print(A)
# elemwise_mat = np.einsum('ij,ij->', A, B)
# print(elemwise_mat)


A = np.array([[1, 2, 3], [4, 5, 6]])
x = np.array([-1, -10, -100])
b = np.einsum('ij,j->i', A, x)
print(b)

# A = np.array([[1, 2, 3], [4, 5, 6]])
# row_sum = np.einsum("ij->i", A)
# col_sum = np.einsum("ij->j", A)
# print(row_sum)
# print(col_sum)


x = np.array([-1, -10, -100])
y = np.array([1, 10, 100])
dot = np.einsum('i,i->', x, y)
outer = np.einsum('i,j->ij', x, y)
print(dot)
print(outer)

x = np.array([-1, -10, -100])
y = np.array([1, 10, 100])
elemwise_vec = np.einsum('i,i->i', x, y)
print(elemwise_vec)
A = np.arange(6).reshape((2, 3))
B = np.arange(6).reshape((2, 3))
elemwise_mat = np.einsum('ij,ij->', A, B)
print(elemwise_mat)

A = np.array([[1, 2, 3], [4, 5, 6]])
x = np.array([-1, -10, -100])
b = np.einsum('ij,j->i', A, x)
print(b)

# Matrix-Matrix Multiplication
A = np.array([[1, 2, 3], [4, 5, 6]])
B = A.transpose()
R = np.einsum('ik,kj->ij', A, b)

# Batched Matrix Multiplication
A = np.random.random(size=(3, 10, 4))
B = np.random.random(size=(3, 4, 8))

R = np.einsum('bik,bkj->bij', A, B)

x = np.array([1, 2, 3])
y = np.array([-1, -2, -3])
A = np.random.random(size=(3, 3))

r = np.einsum('i,ij,j->', x, A, y)
