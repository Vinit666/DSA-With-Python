# method 1 --->bruteforce solution
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        self.head = n1
        if not self.head:
            print("SLL is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def oddEvenLL(self):
        self.head = n1
        temp = self.head
        l = []
        if temp is None and temp.next is None:
            return temp
        while temp is not None and temp.next is not None:
            l.append(temp.val)
            temp = temp.next.next

        temp = self.head.next
        while temp is not None and temp.next is not None:
            l.append(temp.val)
            temp = temp.next.next
        l.append(temp.val)
        # return l
        temp = self.head
        i = 0
        while temp is not None:
            temp.val = l[i]
            temp = temp.next
            i += 1


s1 = SinglyLinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(44)
n5 = Node(99)
n6 = Node(9)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = None

print(f"linked list is :", end=" ")
s1.traversal()

s1.oddEvenLL()

print(f"odd even linked list is :", end=" ")
s1.traversal()


# # method 2 --->optimal solution
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

#     def oddEvenLL(self):
#         odd = self.head
#         even = self.head.next
#         even_head = self.head.next
#         if odd is None or even is None:
#             return odd
#         while even is not None and even.next is not None:
#             odd.next = odd.next.next
#             odd = odd.next
#             even.next = even.next.next
#             even = even.next
#         odd.next = even_head
#         return


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
# s1.oddEvenLL()
# s1.traversal()
