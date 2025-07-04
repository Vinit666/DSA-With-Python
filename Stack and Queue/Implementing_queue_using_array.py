class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, ele):
        self.items.append(ele)

    def dequeue(self):
        if len(self.items) == 0:
            return "Can't pop item, Queue is empty."
        x = self.items.pop(0)
        return x

    def rear(self):
        if len(self.items) == 0:
            return "Stack is empty."
        return self.items[-1]

    def front(self):
        if len(self.items) == 0:
            return "Stack is empty."
        return self.items[0]

    def size(self):
        if len(self.items) == 0:
            return "Stack is empty."
        return len(self.items)

    def show_queue(self):
        return self.items


s1 = Queue()
print(s1.show_queue())
print(s1.is_empty())
print(s1.size())
print(s1.dequeue())
print(s1.front())
print(s1.rear())
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
s1.enqueue(40)
print(s1.show_queue())
print(s1.size())
print(s1.front())
print(s1.rear())
print(s1.dequeue())
print(s1.size())
print(s1.front())
print(s1.is_empty())
print(s1.show_queue())
