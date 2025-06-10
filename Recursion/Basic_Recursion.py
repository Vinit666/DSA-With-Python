# recursion--->when a func() calls itself.


# def greet(c):
#     if c == 5:
#         return
#     print("Hii, Hellow World")
#     greet(c + 1)


# greet(1)


def greet(c):
    if c == 0:
        return
    print("Hii, Hellow World")
    greet(c - 1)


greet(5)
