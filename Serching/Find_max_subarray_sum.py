# # method 1 --->
# # l = [1, -1, -2, 4, -5, -3, 9, -3, 2, 3, -3, 7, -1, 8, -3, 0, 4]
# l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max = 0
# for i in range(0, len(l) - 1):
#     s = l[i]
#     for j in range(i + 1, len(l)):
#         s += l[j]
#         if max < s:
#             max = s


# print(max)


# method 2 --->
# nums = [1, -1, -2, 4, -5, -3, 9, -3, 2, 3, -3, 7, -1, 8, -3, 0, 4]
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSubArray(nums):
    mx = float("-inf")
    s = 0
    if len(nums) == 1:
        return nums[0]
    for i in range(0, len(nums)):
        s += nums[i]
        mx = max(mx, s)
        if s < 0:
            s = 0
    return mx


print(maxSubArray(nums))
