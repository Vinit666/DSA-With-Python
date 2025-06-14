# # method 1 --->
# l = [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
# mc = 0
# c = 0
# for i in range(0, len(l)):
#     if l[i] == 1:
#         c += 1
#         if mc < c:
#             mc = c

#     else:
#         c = 0
# print(f"Max Consecutives of ones is : {mc}")


# # method 2 --->
# l = [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
# mc = 0
# c = 0
# for i in range(0, len(l)):
#     if l[i] == 1:
#         c += 1
#         if l[len(l) - 1] and mc < c:
#             mc = c
#     elif mc < c:
#         mc = c
#         c = 0
#     else:
#         c = 0

# print(mc)


# method 3 --->
l = [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]


def max_consecutive(l):
    mc = 0
    c = 0
    for i in range(0, len(l)):
        if l[i] == 1:
            c += 1
        else:
            mc = max(mc, c)
            c = 0
    return max(mc, c)


print(max_consecutive(l))
