class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.pre = None


class stackUsingDll:
    def __init__(self):
        self.tail = None
        self.head = None

    def push(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.tail == None:
            return "Stack is empty."
        elif self.tail == self.head:
            x = self.tail.val
            self.head = None
            self.tail = None
            return x
        else:
            x = self.tail.val
            self.tail = self.tail.pre
            self.tail.next = None
            return x

    def show_stack(self):
        if self.head == None:
            return "Stack is empty."
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def top(self):
        if self.head == None:
            return "Stack is empty."
        else:
            return self.tail.val


s1 = stackUsingDll()
s1.show_stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print(s1.top())
print(s1.head.val)
print(s1.tail.val)
s1.show_stack()
print(f"pop value is : {s1.pop()}")
print(s1.head.val)
print(s1.tail.val)
s1.show_stack()
print(s1.top())
print(s1.tail.val)
