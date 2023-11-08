class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            li.append(root.val)
            helper(root.right)

        helper(root)
        return li[k - 1]