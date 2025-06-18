# # method 1 --->
# matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5], [3, 4, 5, 0]]
# rows = len(matrix)
# cols = len(matrix[0])
# print("Original matrix is : ")
# for i in range(0, rows):
#     for j in range(0, cols):
#         print(matrix[i][j], end=" ")
#     print()
# print("----------------")
# for i in range(0, cols):
#     for j in range(rows - 1, -1, -1):
#         print(matrix[j][i], end=" ")
#     print()

# print(matrix)


# # method 2 --->
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)


# class Solution(object):
#     def rotate(self, matrix):
#         rows = len(matrix)
#         cols = len(matrix[0])
#         rotate_matrix = [
#             [matrix[j][i] for j in range(rows - 1, -1, -1)] for i in range(0, cols)
#         ]

#         for i in range(0, rows):
#             for j in range(0, cols):
#                 matrix[i][j] = rotate_matrix[i][j]


# s1 = Solution()
# s1.rotate(matrix)
# print()
# print(matrix)


# method 3 --->
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5], [3, 4, 5, 0]]
rows = len(matrix)
cols = len(matrix[0])
for i in range(0, rows):
    for j in range(0, cols):
        print(matrix[i][j], end=" ")
    print()
print()

# transpose metrix(in place)----->
for i in range(0, rows - 1):
    for j in range(i + 1, cols):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# reverse of transpose metrix(in place)----->
for i in range(0, rows):
    matrix[i].reverse()
print()
for i in range(0, rows):
    for j in range(0, cols):
        print(matrix[i][j], end=" ")
    print()
