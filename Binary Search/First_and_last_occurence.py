# #method 1 --->
# nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 10, 10, 10]
# n = len(nums)
# target = 10
# lb = -1
# low = 0
# high = n - 1
# while low <= high:
#     mid = (low + high) // 2
#     if nums[mid] >= target:
#         lb = mid
#         high = mid - 1
#     else:
#         low = mid + 1

# if lb == -1 or nums[lb] != target:
#     print(f"[{-1},{-1}]")
# else:
#     ub = n
#     low = 0
#     high = n - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] > target:
#             ub = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     print(f"[{lb},{ub}]")


# method 2 --->
class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        result = []
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

        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        else:
            result.append(lb)
            ub = n
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1
        if ub == -1:
            ub = n
        result.append(ub - 1)
        return result


s1 = Solution()
print(s1.searchRange(nums=[5, 7, 7, 8, 8, 10], target=20))
