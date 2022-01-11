import numpy as np

# np.arange(start(default=0), stop, step(default=1))

print(np.arange(3))
# 0에서 3전까지

print(np.arange(3.0))
# 실수 타입으로
# 0에서 3전까지

print(np.arange(3, 7))
# 3에서 7전까지

print(np.arange(3, 9, 2))
# 3에서 9전까지 2칸씩

print(np.arange(3*4*5*6))
# 0에서 3*4*5*6까지

# print(np.arange(3*4*5*6).reshape((3, 4, 5, 6)))
