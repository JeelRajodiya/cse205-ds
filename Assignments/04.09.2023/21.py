from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'

    def __next__(self):
        return self.next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        newHead = ListNode()
        cur = newHead
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                newHead.next = list1
                list1 = list1.next
            else:
                newHead.next = list2
                list2 = list2.next
            newHead = newHead.next

        if list1 == None:
            newHead.next = list2
        else:
            newHead.next = list1

        return cur.next


c = ListNode(4, None)
b = ListNode(2, c)
a = ListNode(1, b)

c2 = ListNode(4, None)
b2 = ListNode(3, c2)
a2 = ListNode(1, b2)

s = Solution()

print(s.mergeTwoLists(a, a2))
