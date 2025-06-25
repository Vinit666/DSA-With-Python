def func(index, subset):
    global nums
    global result
    n = len(nums)
    if index >= n:
        result.append(subset.copy())
        return
    subset.append(nums[index])
    func(index + 1, subset)
    subset.pop()
    func(index + 1, subset)
    return result


nums = [5, 9, 7]
subset = []
index = 0
result = []
print(func(index, subset))
