import numpy as np

a = np.arange(25).reshape(5, 5)
b = np.arange(5)
c = np.arange(6).reshape(2, 3)

print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
print(b)
# [0 1 2 3 4]
print(c)
# [[0 1 2]
#  [3 4 5]]

# Trace of a matrix:
a1 = np.einsum('ii', a)
a2 = np.einsum(a, [0, 0])
a3 = np.trace(a)
print(a1)
# 60

# Extract the diagonal (requires explicit form):
b1 = np.einsum('ii->i', a)
b2 = np.einsum(a, [0, 0], [0])
b3 = np.diag(a)
print(b1)
# array([ 0,  6, 12, 18, 24])

# Sum over an axis (requires explicit form):
c1 = np.einsum('ij->i', a)
c2 = np.einsum(a, [0, 1], [0])
c3 = np.sum(a, axis=1)
print(c1)
# array([ 10,  35,  60,  85, 110])

# For higher dimensional arrays summing a single axis can be done with ellipsis:
d1 = np.einsum('...j->...', a)
d2 = np.einsum(a, [Ellipsis, 1], [Ellipsis])
print(d1)
# array([ 10,  35,  60,  85, 110])

# Compute a matrix transpose, or reorder any number of axes:
e1 = np.einsum('ji', c)
e2 = np.einsum('ij->ji', c)
e3 = np.einsum(c, [1, 0])
e4 = np.transpose(c)
print(e1)
# array([[0, 3],
#        [1, 4],
#        [2, 5]])

# Vector inner products:
f1 = np.einsum('i,i', b, b)
f2 = np.einsum(b, [0], b, [0])
f3 = np.inner(b, b)
print(f1)
# 30

# Matrix vector multiplication:
g1 = np.einsum('ij,j', a, b)
g2 = np.einsum(a, [0, 1], b, [1])
g3 = np.dot(a, b)
g4 = np.einsum('...j,j', a, b)
print(g1)
# array([ 30,  80, 130, 180, 230])

# Broadcasting and scalar multiplication:
h1 = np.einsum('..., ...', 3, c)
h2 = np.einsum(',ij', 3, c)
h3 = np.einsum(3, [Ellipsis], c, [Ellipsis])
h4 = np.multiply(3, c)
print(h1)
# array([[ 0,  3,  6],
#        [ 9, 12, 15]])

# Vector outer product:
i1 = np.einsum('i,j', np.arange(2)+1, b)
i2 = np.einsum(np.arange(2)+1, [0], b, [1])
i3 = np.outer(np.arange(2)+1, b)
print(i1)
# array([[0, 1, 2, 3, 4],
#        [0, 2, 4, 6, 8]])
