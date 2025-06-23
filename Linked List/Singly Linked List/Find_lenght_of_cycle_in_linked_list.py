# method 1 :---> T.C = O(n) ,S.C =O(n)
# class Node:
#     def _init_(self, val):
#         self.val = val
#         self.next = None


# class Solution:
#     def _init_(self):
#         self.head = None

#     def result(self):
#         self.head = Node1
#         temp = self.head
#         my_dict = dict()
#         travel = 0
#         while temp is not None:
#             if temp.val in my_dict:
#                 return travel - my_dict[temp.val]
#             my_dict[temp.val] = travel
#             travel += 1
#             temp = temp.next
#         return 0


# s1 = Solution()
# Node1 = Node(10)
# Node2 = Node(11)
# Node3 = Node(13)
# Node4 = Node(14)
# Node5 = Node(15)
# Node6 = Node(16)
# Node7 = Node(17)
# Node8 = Node(18)
# Node9 = Node(19)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node5
# Node5.next = Node6
# Node6.next = Node7
# Node7.next = Node8
# Node8.next = Node9
# Node9.next = Node4

# print(s1.result())


# method 2 --->
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def lenght_hasCycle(self):
        self.head = n1
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                cc = 1
                while slow != fast:
                    slow = slow.next
                    cc += 1
                return cc
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
n11.next = n8  # making cycle here
print(s1.lenght_hasCycle())
