def min_bit_flip(start, goal):
    ans = start ^ goal
    flip_count = 0
    for i in range(0, 32):
        if (ans & (1 << i)) != 0:
            flip_count += 1
    return flip_count


print(min_bit_flip(3, 3))
