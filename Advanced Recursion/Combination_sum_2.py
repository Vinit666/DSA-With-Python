# # method 1 --->Bruteforce solution

# class Solution(object):
#     def combi_sum(self, index, total, subset, nums, target, result):
#         if total == target:
#             # subset.sort()
#             result.add(tuple(subset.copy()))
#             return
#         elif total > target:
#             return
#         if index >= len(nums):
#             return
#         sum = total + nums[index]
#         subset.append(nums[index])
#         self.combi_sum(index + 1, sum, subset, nums, target, result)
#         sum = total
#         subset.pop()
#         self.combi_sum(index + 1, sum, subset, nums, target, result)

#     def combinationSum2(self, candidates, target: int):
#         candidates.sort()
#         result = set()
#         self.combi_sum(0, 0, [], candidates, target, result)
#         return list(result)


# s1 = Solution()
# print(s1.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))


# method 2 --->Optimal Solution


class Solution(object):
    def combination(self, index, total, subset, nums, result):

        if total == 0:
            result.append(subset.copy())
            return
        if total < 0:
            return
        if index >= len(nums):
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            sum = total - nums[i]
            self.combination(i + 1, sum, subset, nums, result)
            sum = total
            subset.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        subset = []
        self.combination(0, target, subset, candidates, result)
        return result


s1 = Solution()
print(s1.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
