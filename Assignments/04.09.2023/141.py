from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n = 0
        fast = head
        slow = head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                return True

        return False
