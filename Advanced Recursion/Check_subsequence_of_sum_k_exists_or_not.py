# # method 1 --->
# def backtrack_sub(index, subset):
#     global result
#     global nums
#     global target
#     if index >= len(nums):
#         if sum(subset) == target:
#             result.append(subset.copy())
#             return True
#         else:
#             return False
#     subset.append(nums[index])
#     pick = backtrack_sub(index + 1, subset)
#     if pick == True:
#         return True
#     subset.pop()
#     not_pick = backtrack_sub(index + 1, subset)
#     return not_pick


# nums = [5, 9, 4, 0]
# result = []
# target = 8
# print(backtrack_sub(index=0, subset=[]))


# method 2 ---> Optimal
def func(index, total, subset):
    global nums
    global result
    global target
    n = len(nums)
    if total == target:
        result.append(subset.copy())
        return True
    elif total > target:
        return False

    if index >= n:
        return False
    subset.append(nums[index])
    summ = total + nums[index]
    pick = func(index + 1, summ, subset)
    if pick == True:
        return True
    e = subset.pop()
    summ = total
    not_pick = func(index + 1, summ, subset)
    return not_pick


nums = [5, 9, 4]
subset = []
index = 0
result = []
target = 10
total = 0
print(func(index, total, subset))
