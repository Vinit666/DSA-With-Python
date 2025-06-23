class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def hasCycle(self):
        self.head = n1
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.val
        return None


s1 = SinglyLinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(44)
n5 = Node(99)
n6 = Node(9)
n7 = Node(98)
n8 = Node(65)
n9 = Node(45)
n10 = Node(67)
n11 = Node(39)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n11
n11.next = n4  # making cycle here
print(s1.hasCycle())
