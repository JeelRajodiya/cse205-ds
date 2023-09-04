# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = None
        while head != None:
            nxt = head.next
            head.next = reversedHead
            reversedHead = head
            head = nxt

        return reversedHead


c = ListNode(3, None)
b = ListNode(2, c)
a = ListNode(1, b)

s = Solution()
print(s.reverseList(a))
