# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# rev_l = []


# def reverse_of_arr(l, s, e):
#     if e < s:
#         return rev_l
#     rev_l.append(l[e])
#     return reverse_of_arr(l, s, e - 1)


# print(reverse_of_arr(l, 2, 6))


# method 2-->

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"original list is : {l}")


def reverse_of_array(l, left, right):
    if left >= right:
        return
    l[left], l[right] = l[right], l[left]
    return reverse_of_array(l, left + 1, right - 1)


reverse_of_array(l, 0, len(l) - 1)
print(f"Reversed list is : {l}")
