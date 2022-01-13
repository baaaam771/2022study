# 2022study

## 1. (25 points) Numpy: Tutorial

다음 자료를 참조하여 numpy 기본을공부하시오.
•https://docs.scipy.org/doc/numpy-1.15.0/user/quickstart.html
•https://www.machinelearningplus.com/python/numpy-tutorial-part1-array-python-examples/
•http://web.mit.edu/dvp/Public/numpybook.pdf
•https://docs.scipy.org/doc/numpy-1.11.0/numpy-user-1.11.0.pdf

### 1.1 Numpy: dot, einsum

-다음numpy의 dot의 정의를 이해하고, 예제를 만들어 설명하시오.
•https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.dot.html

-다음 numpy의 einsum의 정의를이해하고, 예제를 만들어 설명하시오. 또한 dot과의 관련도를 예를 들어 설명하시오.
•https://docs.scipy.org/doc/numpy/reference/generated/numpy.einsum.html

### 1.2 Numpy:quiz풀이

다음 퀴즈의 난이도 3단계의 문항 5개 이상을 해결하시오.
https://github.com/rougier/numpy-100

### 1.3 Numpy: 선형방정식 풀기

A가 정방행렬일때, 다음 선형방정식에서 해 x를 구하는 numpy 코드(linearsol.py)를 작성하시오. (main에서는 코드에 대한 테스트도 포함)

> Ax=b

역행렬을 구하는 함수는 다음을 참조하라.
https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.linalg.inv.html
A가 정방행렬이 아닌 일반행렬일 때(A∈R^m×n), Pseudoinverse를 이용하여 위의 선형방정식의 근사해(least squares solution)x를 구하는 numpy코드(leastsquaresol.py)를 작성하시오.(main에서는 코드에 대한 테스트도 포함)
