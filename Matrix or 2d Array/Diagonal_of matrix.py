# print Diagonal(left to right) --->

matrix = [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9], [9, 0, 1, 2]]
rows = len(matrix)
col = len(matrix[0])

for i in range(0, rows):
    for j in range(0, col):
        if i == j:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()


# print Diagonal(right to left) --->

matrix = [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9], [9, 0, 1, 2]]
rows = len(matrix)
col = len(matrix[0])

for i in range(0, rows):
    for j in range(0, col):
        if i + j == rows - 1:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
