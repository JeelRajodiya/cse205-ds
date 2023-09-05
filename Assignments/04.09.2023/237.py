class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:

    def deleteNode(self, node):
        """
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
        node.val = node.next.val
        node.next = node.next.next
        print(node)


c = ListNode(3, None)
b = ListNode(2, c)
a = ListNode(1, b)

s = Solution()
print(s.deleteNode(b))
print(a)
