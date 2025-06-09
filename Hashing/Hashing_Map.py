"""Method--->1"""

# l = [1, 2, 1, 3, 3, 3, 4, 5, 5, 5, 7, 9, 1, 10]
# m = [1, 2, 100, 12, 34, 10, 45, 76, 98]

# hash_list = []


# for i in range(1, 11):
#     hash_list.append(l.count(i))
# print(f"hash list is : {hash_list}")

# for num in m:
#     if num > 0 and num < 11:
#         print(f"{num} in list-l is : {hash_list[num-1]}")
#     else:
#         print(f"{num} in list-l is : 0")


"""Method --->2"""

# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 7]
# m = [10, 111, 1, 9, 5, 67, 2]
# hash_list = [0] * 11
# for i in n:
#     hash_list[i] += 1
# for j in m:
#     if j >= 1 and j <= 10:
#         print(f"{j} : ", hash_list[j])
#     else:
#         print(f"{j} : 0")

""" Method--->3 """

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 7]
m = [10, 111, 1, 9, 5, 67, 2]

hash_d = {}

for i in n:
    # using get method
    hash_d[i] = hash_d.get(n[i], 0) + 1
    # using count method
    # if i not in hash_d:
    #     hash_d[i] = n.count(i)

for x in m:
    if x in hash_d:
        print(f"{x} count in n is : {hash_d[x]}")
    else:
        print(f"{x} count in n is : 0")
