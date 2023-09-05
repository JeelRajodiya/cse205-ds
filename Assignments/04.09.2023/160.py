from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:

    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:
        headACopy = headA
        headBCopy = headB

        lenA = 0
        lenB = 0

        while headACopy:
            lenA += 1
            headACopy = headACopy.next

        while headBCopy:
            lenB += 1
            headBCopy = headBCopy.next
        headACopy = headA
        headBCopy = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                headACopy = headACopy.next
        elif lenA < lenB:
            for i in range(lenB - lenA):
                headBCopy = headBCopy.next

        while headACopy:
            if headACopy == headBCopy:
                return headACopy
            headACopy = headACopy.next
            headBCopy = headBCopy.next

        print(lenA, lenB)
        return None
