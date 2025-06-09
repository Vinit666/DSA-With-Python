# method --1

n = 36

num = n
result = []
for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)
print(f"Factors or Divisors of number {n} are : {result}")

# -----------------------------------------------------------------------------------

# # #method --2

# n = 36

# num = n
# result = []
# for i in range(1, (num // 2) + 1):
#     if num % i == 0:
#         result.append(i)
# result.append(num)
# print(f"Factors or Divisors of number {n} are : {result}")

# -----------------------------------------------------------------------------------

# method --3
from math import *

n = 36

num = n
result = []
for i in range(1, int(sqrt(num)) + 1):
    if num % i == 0:
        result.append(i)
        if num / i not in result:
            result.append(int(num / i))
print(f"Factors or Divisors of number {n} are : {result}")
