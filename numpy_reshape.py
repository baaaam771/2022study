import numpy as np

a = np.arange(1, 13)
# print(a)

print(np.reshape(a, (2, 6)))
print(np.reshape(a, (6, 2)))
# 2차원에서 역순이다 세로 가로
# (줄(행) 갯수, 하나의 차원 안에서 원소의 수)
# 두덩이가 있고 그 안에 6개 이런 느낌

# print(np.reshape(a, (3, 2, 2)))
# print(np.reshape(a, (2, 3, 2)))

print(np.reshape(a, (2, 2, 3)))
# 3차원일 때
# 거꾸로 간다고 생각하면 될 것 같다
# 아니면 앞에서부터
# 큰 두 덩이에 그 안에 두 덩이 안에 3개

b = np.reshape(a, (2, 2, 3))
print(b[0])
print(b[0][0])
print(b[0, 0])
print(b[0, 0, :])
print(b[0][0][2])
print(b[0][0, 2])
print(b[0, 0, 2])
