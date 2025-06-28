class Solution(object):
    def para(self, index, total, nums, result):
        if index >= len(nums):
            if total == 0:
                result.append("".join(nums))
                return
            else:
                return
        nums[index] = "("
        self.para(index + 1, total + 1, nums, result)
        if total > 0:
            nums[index] = ")"
            self.para(index + 1, total - 1, nums, result)

    def generateParenthesis(self, n):
        nums = [""] * (2 * n)
        result = []
        self.para(0, 0, nums, result)
        return result


s1 = Solution()
print(s1.generateParenthesis(n=3))
