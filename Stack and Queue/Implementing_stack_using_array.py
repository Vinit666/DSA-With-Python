class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, ele):
        self.items.append(ele)

    def pop(self):
        if len(self.items) == 0:
            return "Can't pop item, Stack is empty."
        x = self.items.pop()
        return x

    def top(self):
        if len(self.items) == 0:
            return "Stack is empty."
        return self.items[-1]

    def size(self):
        if len(self.items) == 0:
            return "Stack is empty."
        return len(self.items)

    def show_stack(self):
        return self.items


s1 = stack()
print(s1.show_stack())
print(s1.is_empty())
print(s1.size())
print(s1.pop())
print(s1.top())
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print(s1.show_stack())
print(s1.size())
print(s1.top())
print(s1.pop())
print(s1.size())
print(s1.top())
print(s1.is_empty())
print(s1.show_stack())
