n = int(input("To Check Palindrome, Enter a number : "))

num = n
reverse = 0

while num > 0:
    d = num % 10
    reverse = reverse * 10 + d
    num = num // 10

if reverse == n:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
