# # method 1 ---> by sorting the array using sort().
# l = [12, -21, 23, 9, 98, 45, 6, 304, 23, 789, 0]

# l.sort()

# print(f"List is : {l}")
# print(f"Second Largest in List is : {l[-2]}")


# # method 2 -->

# l = [12, -21, 23, 9, 98, 45, 6, 304, 23, 789, 0]
# largest = float("-inf")
# s_largest = float("-inf")

# for i in range(0, len(l)):
#     if l[i] > largest:
#         largest = l[i]
# for i in range(0, len(l)):
#     if l[i] < largest and l[i] > s_largest:
#         s_largest = l[i]
# print(f"List is : {l}")
# print(f"Second Largest in List is : {s_largest}")


"""Optimal Slotion --->"""
# method 3 -->
l = [12, -21, 23, 9, 98, 45, 6, 304, 23, 789, 0, 789]
largest = float("-inf")
s_largest = float("-inf")

for i in range(0, len(l)):
    if l[i] > largest:
        s_largest = largest
        largest = l[i]
    # elif l[i] > s_largest and l[i] !=largest:
    elif l[i] < largest and l[i] > s_largest:
        s_largest = l[i]
print(f"List is : {l}")
print(f"Second Largest in List is : {s_largest}")
