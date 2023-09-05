from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:

    def middleNode(self, head):
        fast = head
        slow = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow


c = ListNode(3, None)
b = ListNode(2, c)
a = ListNode(1, b)

s = Solution()
print(s.middleNode(a))
