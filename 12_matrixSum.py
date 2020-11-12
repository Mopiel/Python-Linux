import random
import numpy as np

matrix_X = []
matrix_Y = []
matrix_number = 3

for i in range(matrix_number):
    x = random.sample(range(1,201), matrix_number)
    y = random.sample(range(1,201), matrix_number)
    matrix_X.append(x)
    matrix_Y.append(y)


result = [[matrix_X[i][j] + matrix_Y[i][j]  for j in range
(len(matrix_X[0]))] for i in range(len(matrix_X))]

X = np.array(matrix_X)
Y = np.array(matrix_Y)
print(X+Y)
print(result)