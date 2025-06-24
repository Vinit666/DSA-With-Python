# # check set or not ---> using left shift
# n = 13
# i = 1
# if n & (1 << i) != 0:
#     print("Ith is set.")
# else:
#     print("Ith is not set.")

# # this is left shift-->
# print(13 << 2)


# check set or not ---> using right shift
n = 13
i = 3
if (1 & (n >> i)) != 0:
    print("Ith is set.")
else:
    print("Ith is not set.")
