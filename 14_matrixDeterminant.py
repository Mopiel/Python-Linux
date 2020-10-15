import random
import numpy as np

matrix_X = []
matrix_number = 4

for i in range(matrix_number):
    x = random.sample(range(1,201), matrix_number)
    matrix_X.append(x)

for i in matrix_X:
    print(i)
print("=============")


det = 0
for i,_i in enumerate(matrix_X):
    pdet = 1
    mdet = 1
    for j,_j in  enumerate(matrix_X[0]):
        n = i+j
        length = len(matrix_X)
        if n >= length:
            n = n-length
        pdet = pdet*matrix_X[n][j]
        mdet = mdet* matrix_X[length-1 - n][j]
    det = pdet - mdet + det
print("Det",det)