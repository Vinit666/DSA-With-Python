# Search insert position in a sorted array --->
nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 10, 10, 10]
n = len(nums)
target = 4
lb = n
low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    else:
        low = mid + 1
print(lb)
