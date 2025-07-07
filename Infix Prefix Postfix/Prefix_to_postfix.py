class PrefixToPostfix:
    def PrefixToPostfix(self, s):
        result = []

        for char in s[::-1]:
            if char.isalnum():
                result.append(char)
            else:
                operand1 = result.pop()
                operand2 = result.pop()

                new_exp = f"{operand1}{operand2}{char}"

                result.append(new_exp)

        return "".join(result)


s1 = PrefixToPostfix()
print(s1.PrefixToPostfix("/-ab*+def"))
