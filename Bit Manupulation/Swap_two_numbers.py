a = 10
b = 90
print(f"A : {a}")
print(f"B : {b}")

a = a ^ b
b = a ^ b  # (a^b)^b== a becuse b^b=0
a = a ^ b  # a^(a^b)== b becuse a^a=0
print("After swaping the numbers : ")
print(f"A : {a}")
print(f"B : {b}")
