class Solution(object):
    def combi_sum(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        if index >= len(nums):
            return
        sum = total + nums[index]
        subset.append(nums[index])
        self.combi_sum(index, sum, subset, nums, target, result)
        sum = total
        subset.pop()
        self.combi_sum(index + 1, sum, subset, nums, target, result)

    def c_sum(self, candidates, target):
        result = []
        self.combi_sum(0, 0, [], candidates, target, result)
        return result


s1 = Solution()
print(s1.c_sum(candidates=[2, 3, 5], target=8))
