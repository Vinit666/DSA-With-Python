"""method - 1"""

# matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# rows = len(matrix)
# cols = len(matrix[0])
# print("Original matrix is : ")
# for i in range(0, rows):
#     for j in range(0, cols):
#         print(matrix[i][j], end=" ")
#     print()


# def mark_inf(matrix, r, c):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     for i in range(0, cols):
#         if matrix[r][i] != 0:
#             matrix[r][i] = float("inf")
#     for j in range(0, rows):
#         if matrix[j][c] != 0:
#             matrix[j][c] = float("inf")


# def set_zero(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     for i in range(0, rows):
#         for j in range(0, cols):
#             if matrix[i][j] == float("inf"):
#                 matrix[i][j] = 0
#     return matrix

# # marking inf in the matrix --->
# for i in range(0, rows):
#     for j in range(0, cols):
#         if matrix[i][j] == 0:
#             mark_inf(matrix, i, j)

# # marking zeros where the inf in the matrix --->
# for i in range(0, rows):
#     for j in range(0, cols):
#         if matrix[i][j] == 0:
#             set_zero(matrix)


# print(f"Updated matrix is : {matrix}")


""" method - 2 """
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
rows = len(matrix)
cols = len(matrix[0])
print("Original matrix is : ")
for i in range(0, rows):
    for j in range(0, cols):
        print(matrix[i][j], end=" ")
    print()

row_track = [0 for _ in range(0, rows)]
col_track = [0 for _ in range(0, cols)]

for i in range(0, rows):
    for j in range(0, cols):
        if matrix[i][j] == 0:
            row_track[i] = -1
            col_track[j] = -1
for i in range(0, rows):
    for j in range(0, cols):
        if row_track[i] == -1 or col_track[j] == -1:
            matrix[i][j] = 0
        else:
            matrix[i][j]
print(f"Updated matrix is : {matrix}")
