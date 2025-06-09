# # method --1

# n = 176965

# cd = len(str(n))
# print(f"Digit count in number {n} is : {cd}")

# ---------------------------------------------------------------------------------------

# # method --2

# n = 176965

# num = n
# d_count = 0

# while num > 0:
#     digit = num % 10
#     d_count += 1
#     num = num // 10
# print(f"Digit count in number {n} is : {d_count}")

# ---------------------------------------------------------------------------------------

# method --3
from math import *

n = 1230766

num = n

d_count = int(log10(num) + 1)
print(f"Digit count in number {n} is : {d_count}")
