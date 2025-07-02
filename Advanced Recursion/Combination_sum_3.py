# method 1 --->
# class Solution:
#     def combination(self, index, k, n, subset, result):

#         if index >= len(nums):
#             if len(subset) == k:
#                 if sum(subset) == n:
#                     result.append(subset.copy())
#             return
#         if sum(subset) > n:
#             return
#         subset.append(nums[index])
#         self.combination(index + 1, k, n, subset, result)
#         subset.pop()
#         self.combination(index + 1, k, n, subset, result)
#         return result

#     def combinationSum3(self, n, k):
#         subset = []
#         result = []
#         self.combination(0, n, k, subset, result)
#         return result


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = []
# subset = []
# s1 = Solution()
# print(s1.combinationSum3(3, 7))


# method 2 --->


class Solution:
    def combination(self, index, nums, subset, result, target, total, k):
        if index >= len(nums):
            if len(subset) == k:
                if total == target:
                    result.append(subset.copy())
            return
        if total > target:
            return
        subset.append(nums[index])
        summ = total + nums[index]
        self.combination(index + 1, nums, subset, result, target, summ, k)
        subset.pop()
        summ = total
        self.combination(index + 1, nums, subset, result, target, summ, k)

    def combinationSum3(self, k: int, n: int):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        subset = []
        self.combination(0, nums, subset, result, n, 0, k)
        return result


s1 = Solution()
print(s1.combinationSum3(3, 7))
