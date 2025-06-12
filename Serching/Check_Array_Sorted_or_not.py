l = [1, 2, 3, 4, 5, 6, 6, 8, 8, 9, 10, 90]


def check_sorted(l):
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


print(check_sorted(l))
