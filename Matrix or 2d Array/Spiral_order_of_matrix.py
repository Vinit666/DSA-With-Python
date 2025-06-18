matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

rows = len(matrix)
col = len(matrix[0])

print("Metrix is : ")
for i in range(0, rows):
    for j in range(0, col):
        print(matrix[i][j], end=" ")
    print()

top = 0
bottom = rows - 1
left = 0
right = col - 1
s_matrix = []

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        s_matrix.append(matrix[top][i])
    top += 1
    for i in range(top, bottom + 1):
        s_matrix.append(matrix[i][right])
    right -= 1
    if top <= bottom:
        for i in range(right, left - 1, -1):
            s_matrix.append(matrix[bottom][i])
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            s_matrix.append(matrix[i][left])
        left += 1
print(s_matrix)
