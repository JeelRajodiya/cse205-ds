from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fastHead = head
        slowHead = head
        middleHead = None
        fastLength = 1
        while fastHead and fastHead.next and slowHead:
            slowHead = slowHead.next
            fastHead = fastHead.next.next
            fastLength += 2

        reversedHead = None
        slowLength = 0
        while slowHead:
            slowLength += 1
            nxt = slowHead.next
            slowHead.next = reversedHead
            reversedHead = slowHead
            slowHead = nxt

        while reversedHead and head:
            if reversedHead.val != head.val:
                return False
            head = head.next
            reversedHead = reversedHead.next
        return True


e = ListNode(1, None)
d = ListNode(2, e)
c = ListNode(5, d)
b = ListNode(1, c)
a = ListNode(1, b)

s = Solution()
print(a)
print(s.isPalindrome(a))