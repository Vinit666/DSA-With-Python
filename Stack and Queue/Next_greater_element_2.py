class Solution:
    def solve(self, lst):
        n = len(lst)
        result = [-1] * n
        stack = []
        for i in range(2 * n - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= lst[i % n]:
                stack.pop()
            if i < n:
                if len(stack) != 0:
                    result[i] = stack[-1]
            stack.append(lst[i % n])
        return result


s1 = Solution()
print(s1.solve([1, 3, 11, 10, 2, 4]))
print(s1.solve([19, 4, 2, 11, 6, 5, 3, 10]))
print(s1.solve([2, 10, 12, 1, 11]))
