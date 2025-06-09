s = "aaaeeeiiiioooouuuu"
m = ["h", "u", "x", "d", "a", "v", "A", "W"]

hash_l = [0] * 26

for ch in s:
    index = ord(ch) - 97
    hash_l[index] += 1
print(hash_l)

for x in m:
    if ord(x) >= 97 and ord(x) <= 122:
        print(f"{x} : {hash_l[ord(x)-97]}")
    else:
        print(f"{x} : 0")
