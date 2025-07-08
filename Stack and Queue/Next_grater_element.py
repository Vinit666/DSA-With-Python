# method 1 ---> Bruteforce solution : T.C.=O(n^2) S.C.=O(1)/O(n), where n=len(ans)

# class Solution:
#     def solve(self, lst):
#         result = [-1] * len(lst)
#         for i in range(0, len(lst)):
#             for j in range(i + 1, len(lst)):
#                 if lst[j] > lst[i]:
#                     result[i] = lst[j]
#                     break

#         return result


# s1 = Solution()
# print(s1.solve([1, 3, 11, 10, 2, 4]))
# print(s1.solve([19, 4, 2, 11, 6, 5, 3, 10]))


# # method 2 ---> optimal solution : T.C.=O(n) S.C.=O(n)/O(2n), where n=len(ans) and n=len(len(stack))


# class Solution:
#     def solve(self, lst):
# result = [-1] * len(lst)
# stack = []
# for i in range(len(lst) - 1, -1, -1):
#     while len(stack) != 0 and stack[-1] <= lst[i]:
#         stack.pop()
#     if len(stack) == 0:
#         stack.append(lst[i])
#     elif lst[i] < stack[-1]:
#         result[i] = stack[-1]
#         stack.append(lst[i])

# return result


# s1 = Solution()
# print(s1.solve([1, 3, 11, 10, 2, 4]))
# print(s1.solve([19, 4, 2, 11, 6, 5, 3, 10]))


# method 3 ---> optimal solution : T.C.=O(n) S.C.=O(n)/O(2n), where n=len(ans) and n=len(stack)


class Solution:
    def solve(self, lst):
        result = [-1] * len(lst)
        stack = []
        for i in range(len(lst) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= lst[i]:
                stack.pop()
            if len(stack) != 0:
                result[i] = stack[-1]
            stack.append(lst[i])
        return result


s1 = Solution()
print(s1.solve([1, 3, 11, 10, 2, 4]))
print(s1.solve([19, 4, 2, 11, 6, 5, 3, 10]))
