def decimal2binary(nums: int) -> str:
    binary = ""
    while nums > 0:
        if nums % 2 == 0:
            binary += "0"
        else:
            binary += "1"
        nums = nums // 2

    return binary[::-1]


print(decimal2binary(1))
