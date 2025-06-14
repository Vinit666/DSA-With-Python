# # method 1 -->
# a1 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 15]
# a2 = [1, 2, 3, 3, 10, 10, 11, 12, 13, 13, 14, 14, 15]
# print(f"List 1 is : {a1}")
# print(f"List 2 is : {a2}")

# wdml = []

# for i in a1:
#     if i not in wdml:
#         wdml.append(i)
# for i in a2:
#     if i not in wdml:
#         wdml.append(i)
# print(f"Merged list of both lists without dublictes is : {wdml}")


# method 2 -->
a1 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 15]
a2 = [1, 2, 3, 3, 10, 10, 11, 12, 13, 13, 14, 14, 15]
print(f"List 1 is : {a1}")
print(f"List 2 is : {a2}")

wdml = []

i = 0
j = 0

while i < len(a1) and j < len(a2):
    if a1[i] <= a2[j]:
        if len(wdml) == 0 or wdml[-1] != a1[i]:
            wdml.append(a1[i])
        i += 1
    else:
        if len(wdml) == 0 or wdml[-1] != a2[j]:
            wdml.append(a2[j])
        j += 1
while i < len(a1):
    if len(wdml) == 0 or wdml[-1] != a1[i]:
        wdml.append(a1[i])
    i += 1
while j < len(a2):
    if len(wdml) == 0 or wdml[-1] != a2[j]:
        wdml.append(a2[j])
    j += 1

print(f"Merged list of both lists without dublictes is : {wdml}")
