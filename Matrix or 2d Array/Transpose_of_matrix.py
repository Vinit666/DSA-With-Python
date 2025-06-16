matrix = [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]]
rows = len(matrix)
col = len(matrix[0])

print("Metrix is : ")
for i in range(0, rows):
    for j in range(0, col):
        print(matrix[i][j], end=" ")
    print()
print("-------")
print("Transpose of matrix is : ")
for i in range(0, col):
    for j in range(0, rows):
        print(matrix[j][i], end=" ")
    print()

# using list comprehension --->
T_matrix = [[matrix[j][i] for j in range(0, rows)] for i in range(0, col)]
print(f"\nTranspose matrix is : {T_matrix}")
