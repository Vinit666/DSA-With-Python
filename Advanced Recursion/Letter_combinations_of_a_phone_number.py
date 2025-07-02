# # class Solution:
# #     def combination(self,hash_d,subs,result,index,digits):


# #     def letterCombinations(self,digits):
# #         hash_d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
# hash_d = {
#     2: "abc",
#     3: "def",
#     4: "ghi",
#     5: "jkl",
#     6: "mno",
#     7: "pqrs",
#     8: "tuv",
#     9: "wxyz",
# }
# # print(type(hash_d[3][2]))
# digits = "82"
# r = []
# sub = ""
# # i = 0
# # if digits[i] in hash_d:
# #     j = 0
# #     sub += hash_d[digits[i]]
# #     while j < len(hash_d[digits[i]]):
# #         sub += hash_d[digits[i]][j]
# #         r.append(sub)
# # print(r)
# # print(sub)

# digits = "82"
# r = []
# sub = ""
# i = 0
# while i < len(digits):
#     for k, v in hash_d.items():
#         if digits[i] == k:
#             print(k)
#             print(hash_d[digits[i]])
#             # sub += hash_d[digits[i]][0]
#             # for j in range(0, len(hash_d[digits[i]])):
#             #     print(hash_d[digits[i]])
#     # r.append(sub)

#     i += 1
# print(r)
# print(sub)


class Solution:
    def letter_combi(self, index, result, subset, digits, hash_d):
        if index >= len(digits):
            result.append("".join(subset))
            return
        for ch in hash_d[digits[index]]:
            subset.append(ch)
            self.letter_combi(index + 1, result, subset, digits, hash_d)
            subset.pop()
        return result


s1 = Solution()
result = []
subset = []
digits = "92"
hash_d = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
print(s1.letter_combi(0, result, subset, digits, hash_d))
