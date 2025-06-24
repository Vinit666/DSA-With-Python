"""1. And operator ---> &"""

for i in range(0, 3):
    for j in range(0, 3):
        print(i & j, end=" ")
    print()

"""2. Or operator ---> |"""

for i in range(0, 3):
    for j in range(0, 3):
        print(i | j, end=" ")
    print()

"""3. Xor operator ---> ^"""

for i in range(0, 3):
    for j in range(0, 3):
        print(i ^ j, end=" ")
    print()

"""4. Not operator ---> ~"""

for i in range(0, 3):
    print(~(i))

"""5. Shift operator ---> << or >>"""
# left shift
print(1 << 2)

# right shift
print(1 >> 1)
