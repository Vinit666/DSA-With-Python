class PostfixToPrefix:
    def PostfixToPrefix(self, s):
        result = []

        for char in s:
            if char.isalnum():
                result.append(char)
            else:
                operand2 = result.pop()
                operand1 = result.pop()

                new_exp = f"{char}{operand1}{operand2}"

                result.append(new_exp)

        return "".join(result)


s1 = PostfixToPrefix()
print(s1.PostfixToPrefix("ab-de+f*/"))
