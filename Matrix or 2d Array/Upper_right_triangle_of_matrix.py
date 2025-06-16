# print upper right triangle --->

matrix = [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9], [9, 0, 1, 2]]
rows = len(matrix)
col = len(matrix[0])

for i in range(0, rows):
    for j in range(0, col):
        if j >= i:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
