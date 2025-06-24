def binary2decimal(binary):
    index = len(binary) - 1
    decimal = 0
    power = 0
    while index >= 0:
        d = int(binary[index]) * (2**power)
        decimal += d
        index -= 1
        power += 1
    return decimal


print(binary2decimal("1011"))
