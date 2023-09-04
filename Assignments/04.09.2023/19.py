from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        list1 = dummy
        list2 = dummy

        # Move list1 n nodes ahead
        for i in range(n + 1):
            list1 = list1.next

        # Move both list1 and list2 until list1 reaches the end
        while list1 is not None:
            list1 = list1.next
            list2 = list2.next

        # Remove the nth node from the end by updating list2's next pointer
        list2.next = list2.next.next

        return dummy.next  # Return the list start


d = ListNode(4, None)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

s = Solution()

print(s.removeNthFromEnd(a, 1))
