# # method 1 --->


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
#         cuurent = self.head
#         pre_node = None

#         while cuurent is not None:
#             front_node = cuurent.next
#             cuurent.next = pre_node
#             pre_node = cuurent
#             cuurent = front_node
#         self.head = pre_node

#     def hasCycle(self):
#         current = self.head
#         s = set()

#         while current is not None:
#             if current not in s:
#                 s.add(current)
#                 current = current.next
#             else:
#                 return True
#         else:
#             return False


# s1 = SinglyLinkedList()
# s1.append(2)
# s1.append(4)
# s1.append(6)
# s1.append(8)
# s1.append(10)
# s1.traversal()
# print(s1.hasCycle())


# method 2 --->


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

    def hasCycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


s1 = SinglyLinkedList()
s1.append(2)
s1.append(4)
s1.append(6)
s1.append(8)
s1.append(10)
s1.traversal()
print(s1.hasCycle())
