# method 1 ---> T.C. = O(n), S.C. = O(n/2+1)
l = [1, 2, 2, 3, 1, 4, 5, 4, 6, 5, 6]
s = dict()
for i in l:
    s[i] = s.get(i, 0) + 1

for key in s:
    if s[key] == 1:
        print(key)

# method 2 ---> T.C. = O(n), S.C. = O(1)
l = [1, 2, 2, 3, 1, 4, 5, 4, 6, 5, 6, 3, 9]
ans = 0
for i in l:
    ans = ans ^ i
print(ans)
