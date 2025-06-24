# # method 1 --->
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def traversal(self):
#         self.head = n1
#         if not self.head:
#             print("SLL is empty.")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.val, end=" ")
#                 current = current.next
#             print()

#     def Remove_nth(self, n):
#         self.head = n1
#         temp = self.head
#         lenghh_ll = 0

#         while temp is not None:
#             lenghh_ll += 1
#             temp = temp.next

#         if lenghh_ll == n:
#             self.head = n1
#             self.head = self.head.next
#             temp = self.head
#             while temp is not None:
#                 print(temp.val, end=" ")
#                 temp = temp.next
#             print()
#         else:
#             temp = self.head
#             c = 1
#             print((lenghh_ll - n) + 1)
#             while c < (lenghh_ll - n):
#                 temp = temp.next
#                 c += 1
#             temp.next = temp.next.next


# s1 = SinglyLinkedList()
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(44)
# n5 = Node(99)
# n6 = Node(9)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = None
# s1.traversal()
# s1.Remove_nth(n=6)
# s1.traversal()


# method 2 --->
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class singlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
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

    def Remove_nth(self, n):
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            self.head = self.head.next
        else:
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next


s1 = singlyLinkedList()

s1.append(1)
s1.append(2)
s1.append(3)
s1.append(4)
s1.append(5)
s1.traversal()
s1.Remove_nth(n=5)
s1.traversal()
