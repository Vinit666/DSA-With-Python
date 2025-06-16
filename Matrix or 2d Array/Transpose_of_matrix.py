matrix = [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9], [9, 0, 1, 2]]
rows = len(matrix)
col = len(matrix[0])
print("Metrix is : ")
for i in range(0, rows):
    for j in range(0, col):
        print(matrix[i][j], end=" ")
    print()
print("-------")
print("Transpose of matrix is : ")
for i in range(0, rows):
    for j in range(0, col):
        print(matrix[j][i], end=" ")
    print()

T_matrix = [[matrix[j][i] for j in range(0, col)] for i in range(0, rows)]
print(f"\nTranspose matrix is : {T_matrix}")
