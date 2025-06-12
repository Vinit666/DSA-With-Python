# # method 1 -->
# l = [12, -21, 23, 9, 98, 45, 6, 304, 23, 789, 0]
# largest = l[0]
# for i in range(0, len(l)):
#     if largest < l[i]:
#         largest = l[i]
# print(f"List is : {l}")
# print(f"Largest in the list is : {largest}")


# method 2 -->
l = [12, -21, 23, 9, 98, 45, 6, 304, 23, 789, 0]
largest = float("-inf")
for i in range(0, len(l)):
    largest = max(largest, l[i])

print(f"List is : {l}")
print(f"Largest in the list is : {largest}")
