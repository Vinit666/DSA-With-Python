# method 1 --->bruteforce solution

# class Solution:
#     def subset_sum(self, index, nums, subset, result):
#         if index >= len(nums):
#             if subset == []:
#                 result.append(0)
#             return

#         subset.append(nums[index])
#         result.append(sum(subset))
#         self.subset_sum(index + 1, nums, subset, result)
#         subset.pop()
#         self.subset_sum(index + 1, nums, subset, result)
#         return result


# s1 = Solution()
# result = []
# print(s1.subset_sum(0, [5, 9, 3], [], result))


# # method 2 --->optimal solution


# class Solution:
#     def subset_sum(self, index, nums, total, result):
#         if index >= len(nums):
#             if total == 0:
#                 result.append(0)
#             return
#         total += nums[index]
#         result.append(total)
#         self.subset_sum(index + 1, nums, total, result)
#         e = nums[index]
#         self.subset_sum(index + 1, nums, total - e, result)
#         return result


# s1 = Solution()
# result = []
# print(s1.subset_sum(0, [1, 2, 3], 0, result))


# method 3 --->optimal solution


class Solution:
    def subset_sum(self, index, nums, total, result):
        if index >= len(nums):
            result.append(total)
            return
        total += nums[index]
        self.subset_sum(index + 1, nums, total, result)
        e = nums[index]
        self.subset_sum(index + 1, nums, total - e, result)
        return result


s1 = Solution()
result = []
print(s1.subset_sum(0, [1, 2, 3], 0, result))
