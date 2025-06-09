# #method --1

# n = 657657

# num = n
# result = 0
# while num > 0:
#     d = num % 10
#     result = result * 10 + d
#     num = num // 10
# print(f"Reverse of number {n} is : {result}")

# method --2

n = 657657

num = n
while num > 0:
    d = num % 10
    print(d, end="")
    num = num // 10
