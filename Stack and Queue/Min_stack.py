class MinStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, ele):
        if len(self.items) == 0:
            self.items.append([ele, ele])
        else:
            mini = min(self.items[-1][1], ele)
            self.items.append([ele, mini])

    def pop(self):
        if len(self.items) == 0:
            return "Can't pop item, Stack is empty."
        x = self.items[-1][0]
        self.items.pop()
        return x

    def top(self):
        if len(self.items) == 0:
            return "Stack is empty."
        return self.items[-1][0]

    def size(self):
        if len(self.items) == 0:
            return "Stack is empty."
        return len(self.items)

    def show_stack(self):
        return self.items

    def min_stack(self):
        return self.items[-1][1]


s1 = MinStack()
print(s1.show_stack())
print(s1.is_empty())
print(s1.size())
print(s1.pop())
print(s1.top())
s1.push(10)
s1.push(15)
s1.push(4)
s1.push(6)
s1.push(3)
s1.push(1)
s1.push(-4)

print(s1.show_stack())
print(s1.min_stack())
print(s1.size())
print(s1.top())
print(s1.pop())
print(s1.size())
print(s1.top())
print(s1.is_empty())
s1.push(20)
print(s1.show_stack())
print(s1.min_stack())
