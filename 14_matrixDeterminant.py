import random
import numpy as np

matrix_X = []
matrix_number = random.randint(1,50)

for i in range(matrix_number):
    x = random.sample(range(1,201), matrix_number)
    matrix_X.append(x)

print(matrix_X)
X = np.array(matrix_X)
det = round(np.linalg.det(X))
print(det)