# method 1---> if array is not sorted
# l = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7]
# print(f"List is : {l}")

# wdl = []
# for i in l:
#     if i not in wdl:
#         wdl.append(i)
# l = wdl
# print(f"Without Dublicates List is : {l}")


# # method 2---> if array is not sorted
# l = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7]

# def del_dublicates(l):
#     for i in range(0, len(l) - 1):
#         for j in range(i + 1, len(l) - 1):
#             if l[i] == l[j]:
#                 del l[j]
#                 return del_dublicates(l)
#     return l


# print(del_dublicates(l))


# # method 3---> if array is sorted then print no. of unique values in list.
# nums = [2, 3, 4, 5, 7, 87, 87, 87, 90, 90, 90]


# def remove_duplicates(nums):
#     i = 0
#     j = i + 1
#     n = len(nums)

#     if n == 1:
#         return 1

#     while j < n:
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#         j += 1
#     return i + 1


# print(remove_duplicates(nums))


# # method 3---> if array is not sorted then print no. of unique values in list.

nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7]
print(f"Original list is : {nums}")


wdl = {}
for i in range(0, len(nums)):
    wdl[nums[i]] = 0
j = 0
for k in wdl:
    nums[j] = k
    j += 1

print(f"Updated list is : {nums}")
print(f"Unique values in list is : {j}")
