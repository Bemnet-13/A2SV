n = 5

matrix = []

for i in range(1, n + 1):
    arr = []
    for j in range(1, i + 1):
        arr.append(j)
    matrix.append(arr)

for arr in matrix:
    print(*arr)

print('\n \n \n-------------  \n \n \n')

mat = []
for row_val in range(1, n + 1):
    arr = []
    arr.extend([" "] * (row_val - 1))
    for col_val in range(row_val, n + 1):
        arr.append(col_val)
    
    mat.append(arr)



for arr in mat:
    print(*arr)