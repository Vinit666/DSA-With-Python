# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# rows = len(matrix)
# col = len(matrix[0])

# for i in range(0, rows):
#     for j in range(0, col):
#         print(matrix[i][j], end=" ")
#     print()


matrix = [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9], [9, 0, 1, 2]]
rows = len(matrix)
col = len(matrix[0])


# # print metrix --->
# for i in range(0, rows):
#     for j in range(0, col):
#         print(matrix[i][j], end=" ")
#     print()


# # print Diagonal(left to right) --->
# for i in range(0, rows):
#     for j in range(0, col):
#         if i == j:
#             print(matrix[i][j], end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # print lower left triangle --->
# for i in range(0, rows):
#     for j in range(0, col):
#         if i >= j:
#             print(matrix[i][j], end=" ")
#     print()


# print lower right triangle --->
for i in range(0, rows):
    for j in range(0, col):
        if i + j >= rows - 1:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()

"""for i in range(0, rows):
    for j in range(rows - (i + 1), col):
        print(matrix[i][j], end=" ")
    print()"""


# # print upper right triangle --->
# for i in range(0, rows):
#     for j in range(0, col):
#         if j >= i:
#             print(matrix[i][j], end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # print upper left triangle --->
# for i in range(0, rows):
#     for j in range(0, col - i):
#         print(matrix[i][j], end=" ")
#     print()
