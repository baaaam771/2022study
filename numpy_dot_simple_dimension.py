import numpy as np

# 1차원
a1 = np.dot(3, 4)
print(a1)
# 3*4

a = [1, 2]
b = [3, 9]

c = np.dot(a, b)
print(c)
# 1*3+2*9

# 2차원
a2 = [[1, 2],
      [3, 4]]
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

a4 = np.arange(2*3*4).reshape((2, 3, 4))
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]] (2, 3, 4)
b4 = np.arange(2*3*4).reshape((2, 4, 3))
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]
#   [ 9 10 11]]
#  [[12 13 14]
#   [15 16 17]
#   [18 19 20]
#   [21 22 23]]] (2, 4, 3)


print(np.dot(a4, b4), np.dot(a4, b4).shape)  # (2,3,4)*(2,4,3)=(2,3,2,3)
# [[[[  42   48   54]
#    [ 114  120  126]]
#   [[ 114  136  158]
#    [ 378  400  422]]
#   [[ 186  224  262]
#    [ 642  680  718]]]
#  [[[ 258  312  366]
#    [ 906  960 1014]]
#   [[ 330  400  470]
#    [1170 1240 1310]]
#   [[ 402  488  574]
#    [1434 1520 1606]]]] (2, 3, 2, 3)
