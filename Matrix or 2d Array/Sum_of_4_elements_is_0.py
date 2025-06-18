# # method 1 --->
# nums = [1, 2, 0, -1, -1, 2, 3, 0, -3]
# s = set()
# for i in range(0, len(nums)):
#     for j in range(i + 1, len(nums)):
#         for k in range(j + 1, len(nums)):
#             for l in range(k + 1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] + nums[l] == 0:
#                     temp = [nums[i], nums[j], nums[k], nums[l]]
#                     temp.sort()
#                     s.add(tuple(temp))
# result = [list(i) for i in s]
# print(f"list is : {result}")


# # method 2 --->
# l = [0, 1, 2, -1, -1, 4, 2, 3, -3]
# s = set()
# for i in range(0, len(l)):
#     my_set = set()
#     for j in range(i + 1, len(l)):
#         for k in range(j + 1, len(l)):
#             fourth = -(l[i] + l[j] + l[k])
#             if fourth in my_set:
#                 temp = [l[i], l[j], l[k], fourth]
#                 temp.sort()
#                 s.add(tuple(temp))
#             my_set.add(l[j])
# result = [list(i) for i in s]
# print(f"list is : {result}")


# method 3 --->
l = [0, 1, 2, -1, -1, 4, 2, 3]
n = len(l)
l.sort()
result = []
for i in range(0, n):
    if i != 0 and l[i] == l[i - 1]:
        continue
    j = i + 1
    k = n - 1
    while j < k:
        total = l[i] + l[j] + l[k]
        if total < 0:
            j += 1
        elif total > 0:
            k -= 1
        else:
            temp = [l[i], l[j], l[k]]
            result.append(temp)
            j += 1
            k -= 1
        while j < k and l[j] == l[j - 1]:
            j += 1
        while j < k and l[k] == l[k + 1]:
            k -= 1
print(f"list is : {result}")
