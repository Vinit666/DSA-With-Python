# #method--1

# n = [1, 2, 1, 1, 4, 5, 1, 5]


# f_map = {}
# for i in n:
#     if i in f_map:
#         f_map[i] += 1
#     else:
#         f_map[i] = 1

# print(f"List n is : {n}")
# print(f"Frequency Map of List n is : {f_map}")


# method--2

n = [1, 2, 1, 1, 4, 5, 1, 5]


f_map = {}

for i in range(0, len(n)):
    f_map[n[i]] = f_map.get(n[i], 0) + 1

print(f"List n is : {n}")
print(f"Frequency Map of List n is : {f_map}")
