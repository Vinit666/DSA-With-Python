def minsearch_rsa(nums):
    mini = float("inf")
    n = len(nums)
    low = 0
    high = n - 1
    ti = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= nums[high]:
            mini = min(mini, nums[mid])
            high = mid - 1
        else:
            mini = min(mini, nums[mid])
            low = mid + 1
    return mini


print(minsearch_rsa(nums=[17, 18, 20, -4, -2, -1, 0, 16, 17, 17]))
