class PrefixToInfix:
    def prefixToInfix(self, s):
        s = s[::-1]
        result = []

        for char in s:
            if char.isalnum():
                result.append(char)
            else:
                operand1 = result.pop()
                operand2 = result.pop()

                new_exp = f"({operand1}{char}{operand2})"

                result.append(new_exp)

        return "".join(result)


s1 = PrefixToInfix()
print(s1.prefixToInfix("+-*+abcdf"))
print(s1.prefixToInfix("+a*b-^cde"))
