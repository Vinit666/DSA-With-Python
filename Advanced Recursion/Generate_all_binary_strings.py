"""# n = 0
# while n < 16:
#     nums = n
#     binary = ""
#     while nums > 0:
#         if nums % 2 == 0:
#             binary += "0"
#         else:
#             binary += "1"
#         nums = nums // 2

#     print(f"{binary[::-1]}\n")
#     n += 1"""


def gen_binary(nums, index, flag, result):
    if index >= len(nums):
        result.append("".join(nums))
        return
    nums[index] = "0"
    gen_binary(nums, index + 1, True, result)
    if flag == True:
        nums[index] = "1"
        gen_binary(nums, index + 1, False, result)
        nums[index] = "0"


nums = ["0", "0", "0"]
result = []
gen_binary(nums, 0, True, result)
print(result)


# def all_binary():
#     nums = ["0", "0", "0"]
#     result = []
#     gen_binary(nums, 0, True, result)
#     print(result)


# all_binary()
