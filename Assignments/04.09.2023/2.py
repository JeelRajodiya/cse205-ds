from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'

    def fromList(self, list):
        for i in list:
            self.next = ListNode(i)
            self.next = self.next.next


# 1 5 6 9
# 5 2 3 9
#=6 8 0 8
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:

        newNode = ListNode()
        curr = newNode
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        curr.next = ListNode(carry) if carry else None
        return newNode.next


c = ListNode(4, None)
b = ListNode(2, c)
a = ListNode(1, b)

c2 = ListNode(4, None)
b2 = ListNode(3, c2)
a2 = ListNode(1, b2)

s = Solution()

print(s.addTwoNumbers(a, a2))
