# # method 1 --->
# l = [7, 2, 1, 5, 6, 4, 8]
# p = 0
# for i in range(0, len(l)):
#     for j in range(i + 1, len(l)):
#         if l[j] > l[i]:
#             if p < l[j] - l[i]:
#                 p = l[j] - l[i]


# print(p)


# method 2 --->
prices = [7, 2, 1, 5, 6, 4, 8]

n = len(prices)
mx_profit = 0
min_profit = float("inf")
for i in range(0, n):
    min_profit = min(min_profit, prices[i])
    mx_profit = max(mx_profit, prices[i] - min_profit)
print(mx_profit)
