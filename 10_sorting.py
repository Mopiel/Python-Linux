
import random

numbers = random.randint(range(1,101), 50)
print("Init numbers")
print(numbers)

sorted = []

for n in numbers:
    res = len(sorted)
    for id,sortedValue in enumerate(sorted):
        if(sortedValue>n):
            res = id
            break
    sorted.insert(res,n)

print("Sorted Numbers")
print(sorted)