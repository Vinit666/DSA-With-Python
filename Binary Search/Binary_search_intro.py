# binary search---> T.C.= O(Log2(N)), S.C. = O(1)
"""method 1 ---> Iterative Solution"""

# nums = [1, 2, 6, 9, 10, 13, 15, 20, 30, 31, 40, 100, 879, 999, 1000, 2000]
# # nums.sort()
# target = 9999
# n = len(nums)
# low = 0
# high = n - 1
# while low <= high:
#     mid = (low + high) // 2
#     if target == nums[mid]:
#         print(f"index is : {mid}")
#         break
#     elif target > nums[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1
# else:
#     print("-1")


# # method 1.2 --->
# def binary_s(nums, target):
#     low1 = 0
#     high1 = len(nums) - 1
#     while low1 <= high1:
#         mid = (low1 + high1) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             high1 = mid - 1
#         elif nums[mid] < target:
#             low1 = mid + 1
#     return -1


# print(binary_s(nums=[2, 4, 0, 7, 9, 11, 18, 19], target=6))


""" method 2 ---> Recursive Solution"""


def b_search(nums, target, low, high):
    nums.sort()
    if low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return b_search(nums, target, low=mid + 1, high=n - 1)
        else:
            return b_search(nums, target, low, high=mid - 1)
    else:
        return -1


nums = [1, 2, 6, 9, 10, 13, 15, 20, 30, 31, 40, 100, 879, 999, 1000, 2000]
n = len(nums)
print(b_search(nums, target=9999, low=0, high=n - 1))
