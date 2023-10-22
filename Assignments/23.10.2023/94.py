# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recursion(self, root: Optional[TreeNode], arr: List):

        if root and root.left:
            self.recursion(root.left, arr)
        if root:
            arr.append(root.val)
            print(root.val)
        if root and root.right:
            self.recursion(root.right, arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.recursion(root, arr)
        return arr
