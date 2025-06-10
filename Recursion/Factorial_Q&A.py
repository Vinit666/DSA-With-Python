def factorial_of(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_of(n - 1)


num = int(input("For Factorial, Enter a number(Positive Integer Only) : "))
print(factorial_of(num))
