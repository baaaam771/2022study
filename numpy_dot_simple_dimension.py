import numpy as np

# 1차원
a1 = np.dot(3, 4)
print(a1)
# 3*4

a = [1, 2]
b = [2, 3]

c = np.dot(a, b)
print(c)
# 1*2+2*3

# 2차원
a2 = [[1, 0],
      [0, 1]]
b2 = [[4, 1],
      [2, 2]]

c2 = np.dot(a2, b2)
print(c2)
# array([[4, 1],
#    [2, 2]])
# 행렬 계산


a3 = np.arange(2*3).reshape((2, 3))
print(a3, a3.shape)
# [[0 1 2]
#  [3 4 5]] (2, 3)

b3 = np.arange(3*4).reshape((3, 4))
print(b3, b3.shape)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]] (3, 4)

print(np.dot(a3, b3), np.dot(a3, b3).shape)  # (2,3)*(3,4)=(2,4)
# [[20 23 26 29]
#  [56 68 80 92]] (2, 4)
