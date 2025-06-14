# #method 1 --->
# l = [1, 2, 0, 3, 4, 5, 6, 9, 7]

# for i in range(0, len(l) + 1):
#     if i not in l:
#         print(i)
#         break


# # method 2 --->
# l = [1, 2, 0, 3, 4, 5, 6, 9, 7]
# freq = {}
# for i in range(0, len(l) + 1):
#     freq[i] = 0
# for i in range(0, len(l)):
#     freq[l[i]] = 1
# for k, v in freq.items():
#     if v == 0:
#         print(f"Missing number is : {k}")


# # method 3 --->
# l = [1, 2, 0, 3, 4, 5, 6, 9, 7]
# i_sum = 0
# l_sum = 0
# for i in range(0, len(l)):
#     i_sum += i + 1
#     l_sum += l[i]


# print(f"Missing number is : {i_sum - l_sum}")


# # method 4 --->
# l = [1, 2, 0, 3, 4, 5, 6, 9, 7]
# i_sum = 0
# for i in range(0, len(l) + 1):
#     i_sum += i

# print(f"Missing number is : {i_sum - sum(l)}")

# method 5--->
l = [1, 2, 0, 3, 4, 5, 6, 9, 7]
n = len(l)
print(f"Missing number is : {n*(n+1)//2 - sum(l)}")
