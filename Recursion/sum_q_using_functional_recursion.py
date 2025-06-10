# sum q using functional recursion--->


# #method 1-->
# def func(sum, i, n):
#     if i > n:
#         print(f"sum is : {sum}")
#         return
#     return func(sum + i, i + 1, n)


# func(0, 1, 10)


# # method 2-->
# def func(i, n):
#     if i > n:
#         return 0
#     return i + func(i + 1, n)


# print(func(3, 10))


# method 3-->
def func(n):
    if n == 1:
        return 1
    return n + func(n - 1)


print(func(11))
