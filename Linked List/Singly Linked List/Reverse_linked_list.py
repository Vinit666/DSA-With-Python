# # method 1 ---> using stack


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def traversal(self):
#         if not self.head:
#             print("SLL is empty.")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.val, end=" ")
#                 current = current.next
#             print()

#     def rll(self):
#         stack = []
#         cuurent = self.head
#         pre_node = None
#         while cuurent is not None:
#             stack.append(cuurent.val)
#             cuurent = cuurent.next

#         cuurent = self.head
#         while cuurent is not None:
#             cuurent.val = stack.pop()
#             cuurent = cuurent.next


# s1 = SinglyLinkedList()
# s1.append(2)
# s1.append(4)
# s1.append(6)
# s1.append(8)
# s1.append(10)
# s1.traversal()
# print(s1.head.val)
# s1.rll()
# print()
# s1.traversal()
# print(s1.head.val)


# method 2 ---> optimal solution


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        if not self.head:
            print("SLL is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def rll(self):
        cuurent = self.head
        pre_node = None

        while cuurent is not None:
            front_node = cuurent.next
            cuurent.next = pre_node
            pre_node = cuurent
            cuurent = front_node
        self.head = pre_node


s1 = SinglyLinkedList()
s1.append(2)
s1.append(4)
s1.append(6)
s1.append(8)
s1.append(10)
s1.traversal()
print(s1.head.val)
s1.rll()
print()
s1.traversal()
print(s1.head.val)
