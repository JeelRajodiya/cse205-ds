# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rec(self, root, val):
        if not root:
            root = TreeNode(val)
            return root
        rval = root.val
        if rval < val:
            root.right = self.rec(root.right, val)
        else:
            root.left = self.rec(root.left, val)
        return root

    def insertIntoBST(self, root: Optional[TreeNode],
                      val: int) -> Optional[TreeNode]:
        return self.rec(root, val)
