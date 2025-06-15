# #method 1 --->
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# cc = 0

# for i in range(0, len(nums)):
#     s = nums[i]
#     c = 1
#     while s + 1 in nums:
#         c += 1
#         s += 1
#     cc = max(cc, c)


# print(cc)


# # method 2 --->
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# hash_set = set()
# for i in range(0, len(nums)):
#     hash_set.add(nums[i])

# maxx = 0
# for i in hash_set:
#     c = 0
#     if i - 1 not in hash_set:
#         s = i
#         c += 1
#         while s + 1 in hash_set:
#             c += 1
#             s += 1
#     maxx = max(maxx, c)
# print(maxx)


# method 3 --->
nums = [11, 0, 3, 7, 2, 8, 4, 6, 0, 1, 9, 10]
nums.sort()
ls = float("-inf")
c = 0
maxx = 0
for i in range(0, len(nums)):
    num = nums[i]
    if num - 1 == ls:
        ls = num
        c += 1
    elif num != ls:
        c = 1
        ls = num
    maxx = max(maxx, c)
print(maxx)
