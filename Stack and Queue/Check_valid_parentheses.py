# #method 1 --->
# class Solution:
#     def isValid(self, s):
#         sb = 0
#         cb = 0
#         simp = 0

#         for ch in s:
#             if ch == "(" and simp >= 0:
#                 simp += 1
#             elif ch == "[" and sb >= 0:
#                 sb += 1
#             elif ch == "{" and cb >= 0:
#                 cb += 1
#             elif ch == ")":
#                 simp -= 1
#             if ch == "]":
#                 sb -= 1
#             if ch == "}":
#                 cb -= 1

#         if sb == 0 and cb == 0 and simp == 0:
#             return True
#         else:
#             return False


# s1 = Solution()
# print(s1.isValid("({[)})"))


# method 2 ---> Optimal solution
class Solution:

    def __init__(self):
        self.items = []

    def push(self, ele):
        self.items.append(ele)

    def pop(self):
        if len(self.items) == 0:
            return "Can't pop item, Stack is empty."
        x = self.items.pop()
        return x

    def isValid(self, s):
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                self.items.append(ch)
            else:
                if len(self.items) == 0:
                    if ch == ")" or ch == "]" or ch == "}":
                        return False
                elif ch == ")" and self.items[-1] == "(":
                    self.items.pop()
                elif ch == "]" and self.items[-1] == "[":
                    self.items.pop()
                elif ch == "}" and self.items[-1] == "{":
                    self.items.pop()
                else:
                    return False

        if len(self.items) == 0:
            return True
        else:
            return False


s1 = Solution()
print(s1.isValid("()"))
print(s1.isValid("()[]{}"))
print(s1.isValid("([])"))
print(s1.isValid("]"))


# method 3 --->optimal solution
class Solution:
    def isValid(self, s: str) -> bool:
        self.items = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                self.items.append(i)
            else:
                if len(self.items) == 0:
                    return False
                e = self.items.pop()
                if (
                    e == "("
                    and i == ")"
                    or e == "["
                    and i == "]"
                    or e == "{"
                    and i == "}"
                ):
                    continue
                else:
                    return False

        return len(self.items) == 0


s1 = Solution()
