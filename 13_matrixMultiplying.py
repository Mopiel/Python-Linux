import random
import numpy as np

matrix_X = []
matrix_Y = []
matrix_number = 8
result = []

for i in range(matrix_number):
    x = random.sample(range(1,201), matrix_number)
    y = random.sample(range(1,201), matrix_number)
    r = [0]*matrix_number
    matrix_X.append(x)
    matrix_Y.append(y)
    result.append(r)

for i,_i in enumerate(matrix_X):
    for j,_j in enumerate(matrix_X[0]):
        sum = 0
        for n,_n in enumerate(matrix_X):
            sum = matrix_X[i][n]*matrix_Y[n][j] +sum
        result[i][j] = sum
for i in matrix_X:
    print(i)
print("-----------")
for i in matrix_Y:
    print(i)
print("-----------")
for i in result:
    print(i)

X = np.array(matrix_X)
Y = np.array(matrix_Y)

print(np.dot(X,Y))