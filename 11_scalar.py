vector_a = [1,2,12,4]
vector_b = [2,4,2,8]

sum = 0
for id,value in enumerate(vector_a):
    sum = vector_a[id] *vector_b[id] + sum
print(sum)

