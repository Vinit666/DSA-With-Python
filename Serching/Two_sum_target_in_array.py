# #method 1 -->
# l = [1, 2, 3, 4, 5, 6, 7, 9, 0, 10, 78, 4, 3, 3]
# target = 11
# for i in range(0, len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] + l[j] == target:
#             print(f"{i} and {j}")


# # method 2 -->
# l = [1, 2, 6, 7, 9, 0, 10, 78, 4, 3, 3]
# target = 4
# hash_map = {}

# for i in range(0, len(l)):
#     if l[i] < target:
#         hash_map[l[i]] = i

# for i in range(0, len(l)):
#     re = target - l[i]
#     if re in hash_map:
#         print(f"{i} and {hash_map[re]}")


# method 3 -->
l = [1, 3, 6, 7, 9, 0, 10, 78, 4, 3, 3]
target = 4
hash_map = {}

for i in range(0, len(l)):
    re = target - l[i]
    if re in hash_map:
        print(f"{i} and {hash_map[re]}")
    else:
        hash_map[l[i]] = i
