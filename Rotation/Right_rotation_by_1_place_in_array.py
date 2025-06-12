# # method 1 --->
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"Original list is : {l}")
# temp = l[-1]
# for i in range(len(l) - 2, -1, -1):
#     l[i + 1] = l[i]
# l[0] = temp
# print(f"Right Rotated by 1 place list is : {l}")


# method 2 --->
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list is : {l},id : {id(l)}")

l[:] = [l[len(l) - 1]] + l[0 : len(l) - 1]

print(f"Right Rotated by 1 place list is : {l},id : {id(l)}")
