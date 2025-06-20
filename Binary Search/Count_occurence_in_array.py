# # method 1 ---> if array is not sorted
# nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 10, 10, 10]
# n = len(nums)
# target = 10
# oc = 0
# for i in range(0, n):
#     if nums[i] == target:
#         oc += 1
# print(f"Occurence count of {target} is : {oc}")


# method 2 ---> if array is sorted
# nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 10, 10, 10]
# n = len(nums)
# target = 10
# low = 0
# high = n - 1
# lb = -1
# while low <= high:
#     mid = (low + high) // 2
#     if nums[mid] >= target:
#         lb = mid
#         high = mid - 1
#     else:
#         low = mid + 1

# if lb == -1 and nums[lb] != target:
#     print("0")
# else:
#     low = 0
#     high = n - 1
#     ub = n
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] > target:
#             ub = mid
#             high = mid - 1
#         else:
#             low = mid + 1

#     print(f"Occurence count of {target} is : {(ub)-lb}")

"""-------------------------------------same of method 2------------------------------------------"""


# def result(nums, target):
#     n = len(nums)
#     low = 0
#     high = n - 1
#     lb = -1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] >= target:
#             lb = mid
#             high = mid - 1
#         else:
#             low = mid + 1

#     if lb == -1:
#         return 0
#     else:
#         low = 0
#         high = n - 1
#         ub = n
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] > target:
#                 ub = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1

#         return f"Occurence count of {target} is : {(ub)-lb}"


# print(result(nums=[1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10, 10, 10], target=3))


# method 3 ---> if array is sorted
class Solution(object):
    def binary_lb(self, nums, target):
        low = 0
        high = len(nums) - 1
        lb = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def binary_ub(self, nums, target):
        low = 0
        high = len(nums) - 1
        ub = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    def Result(self, nums, target):
        lb = self.binary_lb(nums, target)
        if lb == -1 or nums[lb] != target:
            return 0
        ub = self.binary_ub(nums, target)
        if ub == -1:
            ub = len(nums)
        return ub - lb


s1 = Solution()
print(s1.Result([3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15, 15], 1))
