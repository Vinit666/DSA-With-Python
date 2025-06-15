# method 1 --->
# l = [3, 1, -2, -5, 2, -4]
# nl = []
# pl = []
# re = []

# for i in range(0, (len(l))):
#     if l[i] < 0:
#         nl.append(l[i])
#     else:
#         pl.append(l[i])
# for i in range(0, len(l) // 2):
#     re.append(pl[i])
#     re.append(nl[i])

# print(re)

# # method 2 --->
# l = [3, 1, -2, -5, 2, -4]
# nl = []
# pl = []

# for i in range(0, (len(l))):
#     if l[i] < 0:
#         nl.append(l[i])
#     else:
#         pl.append(l[i])
# for i in range(0, len(pl)):
#     l[2 * i] = pl[i]
#     l[(2 * i) + 1] = nl[i]

# print(l)


# method 3 --->
l = [3, 1, -2, -5, 2, -4]
rl = [0] * len(l)
p = 0
n = 1
for i in range(0, (len(l))):
    if l[i] > 0:
        rl[p] = l[i]
        p += 2
    else:
        rl[n] = l[i]
        n += 2
print(rl)
