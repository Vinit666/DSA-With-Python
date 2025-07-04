from collections import deque

lst = deque()

lst.append(100)
lst.append(90)
lst.append(10)
print(lst)
lst.append(34)
print(lst)
lst.appendleft(3)
print(lst)
lst.pop()
print(lst)
lst.popleft()
print(lst)
