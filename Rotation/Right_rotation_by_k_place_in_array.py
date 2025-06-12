# # method 1 --->
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"Original list is : {l},id : {id(l)}")
# k = 5
# k%=len(l)


# l[:] = l[len(l) - k : len(l)] + l[0 : len(l) - k]

# print(f"Right Rotated by {k} place list is : {l},id : {id(l)}")


# # method 2 --->
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"Original list is : {l},id : {id(l)}")
# k = 5
# k %= len(l)

# for i in range(0, k):
#     e = l.pop()
#     l.insert(0, e)

# print(f"Right Rotated by {k} place list is : {l},id : {id(l)}")


# method 3 --->
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list is : {l},id : {id(l)}")
n = len(l)


def reverse_array(l, left, right):
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return l


k = 109
k %= n

reverse_array(l, n - k, n - 1)
reverse_array(l, 0, n - k - 1)
reverse_array(l, 0, n - 1)
print(f"Right Rotated by {k} place list is : {l},id : {id(l)}")
