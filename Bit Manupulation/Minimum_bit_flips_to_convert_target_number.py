# method 1 --->
def min_bit_flip(start, goal):
    ans = start ^ goal
    flip_count = 0
    for i in range(0, 32):
        if (ans & (1 << i)) != 0:
            flip_count += 1
    return flip_count


print(min_bit_flip(3, 3))


# method 2 --->


def min_bit_flip(start, goal):
    ans = start ^ goal
    flip_count = 0
    while ans > 0:
        if ans % 2 == 1:
            flip_count += 1
        ans = ans // 2
    return flip_count


print(min_bit_flip(10, 7))
