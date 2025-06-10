# method -1 -->

s = input("Enter a String : ")


def palindrome(s, l=0, r=len(s) - 1):
    if l == r:
        return
    elif s[l] == s[r]:
        return "String is a Palindrome."
    elif s[l] != s[r]:
        return "String is not a Palindrome."

    return palindrome(s, l + 1, r - 1)


print(palindrome(s))


# method -2 -->
s = input("Enter a String : ")


def palindrome(s, l=0, r=len(s) - 1):
    if l >= r:
        return "String is a Palindrome."
    elif s[l] != s[r]:
        return "String is not a Palindrome."

    return palindrome(s, l + 1, r - 1)


print(palindrome(s))
