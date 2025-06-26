# method 1 --->
# def func(index, subset):
#     global nums
#     global result
#     global target
#     n = len(nums)
#     if index >= n:
#         if sum(subset) == target:
#             result.append(subset.copy())
#             return
#         else:
#             return
#     subset.append(nums[index])
#     func(index + 1, subset)
#     subset.pop()
#     func(index + 1, subset)
#     return result


# nums = [5, 9, 4, 0]
# subset = []
# index = 0
# result = []
# target = 9
# print(func(index, subset))


# method 2 ---> Optimal
def func(index, total, subset):
    global nums
    global result
    global target
    n = len(nums)
    if total == target:
        result.append(subset.copy())
        return
    if total > target:
        return

    if index >= n:
        return
    if len(result) == 1:
        return True
    else:
        subset.append(nums[index])
        summ = total + nums[index]
        func(index + 1, summ, subset)
        e = subset.pop()
        summ = summ - e
        func(index + 1, summ, subset)


nums = [5, 9, 4]
subset = []
index = 0
result = []
target = 9
total = 0
print(func(index, total, subset))
