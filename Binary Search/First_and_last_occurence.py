nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 10, 10, 10]
n = len(nums)
target = 20
lb = -1
low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    else:
        low = mid + 1

if lb == -1:
    print(f"[{-1},{-1}]")
else:
    ub = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    print(f"[{lb},{ub-1}]")
