"""Parameter recursion--->"""

# #head parameter recursion:
# def func(i, n):
#     if i > n:
#         return
#     print(i)
#     func(i + 1, n)


# func(1, 5)


# # Tail parameter recursion:
# def func(i, n):
#     if i > n:
#         return
#     func(i + 1, n)
#     print(i)


# func(1, 5)

"""
output-->
5
4
3
2
1
"""


# Tail parameter recursion:(Back Tracking)
def func(i, n):
    if i > n:
        return
    func(i + 1, n)
    print(n + 1 - i)


func(1, 5)
