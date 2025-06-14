# #method 1 --->
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 56, 43, 23, 12, 2, 23, 34, 5, 44, 32, 22, 34, 55]
# print(f"List is : {l}")
# x = int(input("Enter a number : "))
# for i in range(0, len(l)):
#     if l[i] == x:
#         print(f"Number at index : {i}")
# if x not in l:
#     print("-1")


# method 2 --->
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 56, 43, 23, 12, 2, 23, 34, 5, 44, 32, 22, 34, 55]
print(f"List is : {l}")


def linear_serach(l):
    x = int(input("Enter a number : "))
    for i in range(0, len(l)):
        if l[i] == x:
            return i
            # return f"Number at index : {i}"
    return -1


print(linear_serach(l))
