Num_tuple = (5, 6, 8, 3, 9, 1)
prod = 1
arr = []
for i in range(len(Num_tuple)):
    prod *= Num_tuple[i]
    arr.append(prod)
print(arr)
