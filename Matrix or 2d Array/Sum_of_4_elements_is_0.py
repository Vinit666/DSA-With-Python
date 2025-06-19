# # method 1 --->
# nums = [1, 2, 0, -1, -1, 2, 3, 0, -3]
# s = set()
# for i in range(0, len(nums)):
#     for j in range(i + 1, len(nums)):
#         for k in range(j + 1, len(nums)):
#             for l in range(k + 1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] + nums[l] == 0:
#                     temp = [nums[i], nums[j], nums[k], nums[l]]
#                     temp.sort()
#                     s.add(tuple(temp))
# result = [list(i) for i in s]
# print(f"list is : {result}")


# # method 2 --->
# l = [0, 1, 2, -1, -1, 4, 2, 3, -3]
# s = set()
# for i in range(0, len(l)):
#     my_set = set()
#     for j in range(i + 1, len(l)):
#         for k in range(j + 1, len(l)):
#             fourth = -(l[i] + l[j] + l[k])
#             if fourth in my_set:
#                 temp = [l[i], l[j], l[k], fourth]
#                 temp.sort()
#                 s.add(tuple(temp))
#             my_set.add(l[j])
# result = [list(i) for i in s]
# print(f"list is : {result}")


# method 3 --->
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
        return result


s1 = Solution()
print(s1.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
