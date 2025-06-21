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
        current = self.head

    def midd(self, head):
        n = len(head)
        current = self.head
        if n % 2 == 0:
            m = n // 2
            cm = 0

            while current is not None:
                if cm >= m:
                    print(current.val, end=" ")
                current = current.next
                cm += 1
        else:
            m = n // 2
            cm = 0
            while current is not None:
                if cm >= m:
                    print(current.val, end=" ")
                current = current.next
                cm += 1


s1 = singlyLinkedList()
head = [1, 2, 3, 4, 5]
for i in head:
    s1.append(i)

# s1.append(1)
# s1.append(2)
# s1.append(3)
# s1.append(4)
# s1.append(5)
# s1.traversal()
s1.midd(head=[1, 2, 3, 4, 5])


""" method 2 --->Leet code Solution """

# class Solution(object):
#     def middleNode(self, head):
#         slow_pointer = head
#         fast_pointer = head

#         while fast_pointer is not None and fast_pointer.next is not None:
#             slow_pointer = slow_pointer.next
#             fast_pointer = fast_pointer.next.next

#         return slow_pointer
