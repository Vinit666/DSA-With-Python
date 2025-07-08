# class Solution:
#     def Solve(self, nums):
#         n = len(nums)
#         s = []
#         for i in range(n):
#             if nums[i] >= 0:
#                 while len(s) != 0 and nums[i] > s[-1]:
#                     s.pop()
#                 s.append(nums[i])
#             else:
#                 while len(s) != 0 and nums[i] > s[-1]:
#                     s.pop()
#                 s.append(nums[i])

#                 if len(s) != 0 and abs(nums[i]) > s[-1]:
#                     s.pop()
#                 elif len(s) != 0 and s[-1] < 0:
#                     s.append(nums[i])
#         return s


# s1 = Solution()
# print(s1.Solve(nums=[4, 7, 1, 1, 2, -3, -7, 17, 15, -18, -19]))


class Solution:
    def Solve(self, nums):
        n = len(nums)
        s = []
        for i in range(n):
            if nums[i] >= 0:
                s.append(nums[i])
            else:
                while len(s) != 0 and s[-1] > 0 and abs(nums[i]) > s[-1]:
                    s.pop()

                if len(s) != 0 and abs(nums[i]) == s[-1]:
                    s.pop()

                if len(s) == 0 or s[-1] < 0:
                    s.append(nums[i])

        return s


s1 = Solution()
print(s1.Solve(nums=[4, 7, 1, 1, 2, -3, -7, 17, 15, -18, -19]))
