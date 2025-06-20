nums = [17, 18, 20, 1, 3, 4, 5, 7, 10, 11, 16]
target = 7
n = len(nums)
low = 0
high = n - 1
ti = -1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        ti = mid
        break
    elif nums[mid] <= nums[high]:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        if nums[low] <= target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
print(ti)

""" same code but sung func() below --->"""


def search_rsa(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ti = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            ti = mid
            break
        elif nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return ti


print(search_rsa(nums=[17, 18, 20, 1, 3, 4, 5, 7, 10, 11, 16], target=10))
