class QueueUsingStack:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def is_empty(self):
        return len(self.st1) == 0

    def enqueue(self, ele):
        for _ in range(len(self.st1)):
            self.st2.append(self.st1.pop())
        self.st1.append(ele)
        for _ in range(len(self.st2)):
            self.st1.append(self.st2.pop())

    def dequeue(self):
        if len(self.st1) == 0:
            return "Can't pop item, Queue is empty."
        x = self.st1.pop()
        return x

    def rear(self):
        if len(self.st1) == 0:
            return "Queue is empty."
        return self.st1[0]

    def front(self):
        if len(self.st1) == 0:
            return "Queue is empty."
        return self.st1[-1]

    def size(self):
        if len(self.st1) == 0:
            return "Queue is empty."
        return len(self.st1)

    def show_queue(self):
        return self.st1


s1 = QueueUsingStack()
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
print(s1.st1)
print(s1.size())
print(s1.front())
print(s1.rear())
print(s1.is_empty())
print(s1.show_queue())
