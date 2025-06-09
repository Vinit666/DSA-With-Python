n = int(input("To Check Armstrong, Enter a Number :"))

num = n
dc = len(str(n))
result = 0
while num > 0:
    d = num % 10
    result += d**dc
    num = num // 10

if result == n:
    print("Yes, it is a Armstrong number.")
else:
    print("No, it is not a Armstrong number.")
