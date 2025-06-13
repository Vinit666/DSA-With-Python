# # method 1 --->
# nums = [1, 0, 2, 0, 1, 0, 1, 0, 4, 0, 0, 3, 0, 0, 0, 3, 5, 0, 3, 1, 0, 9]
# print(nums)


# def Result(nums):
#     for i in range(0, len(nums) - 1):
#         if nums[i] == 0 and nums[i + 1] != 0:
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#             return Result(nums)
#     return nums


# print(Result(nums))

# # method 2 --->
# nums = [1, 0, 2, 0, 1, 0, 1, 0, 4, 0, 0, 3, 0, 0, 0, 3, 5, 0, 3, 1, 0, 9]
# print(nums)


# def remove_zero(nums):
#     for i in range(0, len(nums) - 1):
#         if nums[i] == 0 and nums[i + 1] != 0:
#             nums.append(nums.pop(i))
#             return remove_zero(nums)
#     return nums


# print(remove_zero(nums))


# # method 3 --->
# nums = [1, 0, 2, 0, 1, 0, 1, 0, 4, 0, 0, 3, 0, 0, 0, 3, 5, 0, 3, 1, 0, 9]
# print(nums)
# n = len(nums)
# temp = []

# for i in range(0, n):
#     if nums[i] != 0:
#         temp.append(nums[i])

# m = len(temp) - 1
# for i in range(0, n):
#     if i <= m:
#         nums[i] = temp[i]
#     else:
#         nums[i] = 0
# print(nums)


# method 4 -->
nums = [1, 0, 2, 0, 1, 0, 1, 0, 4, 0, 0, 3, 0, 0, 0, 3, 5, 0, 3, 1, 0, 9]
print(nums)

n = len(nums)


def result(nums):
    if n == 0:
        return nums
    i = 0
    while i < n:
        if nums[i] == 0:
            break
        i += 1
        if i == n:
            return nums
        j = i + 1

    while j < n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums


print(result(nums))
