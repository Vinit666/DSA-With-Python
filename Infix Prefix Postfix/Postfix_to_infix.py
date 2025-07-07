class PostfixToInfix:
    def postfixToInfix(self, s):
        result = []

        for char in s:
            if char.isalnum():
                result.append(char)
            else:
                operand2 = result.pop()
                operand1 = result.pop()

                new_exp = f"({operand1}{char}{operand2})"

                result.append(new_exp)

        return "".join(result)


s1 = PostfixToInfix()
print(s1.postfixToInfix("abcd^e-*+"))
