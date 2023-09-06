from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        lookup = set()
        cur = head
        while cur:
            if cur in lookup:
                return cur
            lookup.add(cur)
            cur = cur.next

        return None


e = ListNode(1, None)
d = ListNode(2, e)
c = ListNode(5, d)
b = ListNode(1, c)
a = ListNode(1, b)
e.next = a

s = Solution()
print(s.detectCycle(a).val)
