nums = [1, 2, 3]
n = len(nums)
ts = 2**n
result = []

for i in range(0, ts):
    lst = []
    for j in range(0, n):
        if i & (1 << j) != 0:
            lst.append(nums[j])
    result.append(lst)
print(result)
