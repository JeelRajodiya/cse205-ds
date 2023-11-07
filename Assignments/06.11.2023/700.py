from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def searchBST(self, root: Optional[TreeNode],
                  val: int) -> Optional[TreeNode]:

        def recursion(root):

            if root:
                if root.val == val:
                    print(root)
                    return root
                if val < root.val:
                    return recursion(root.left)
                else:
                    return recursion(root.right)
            else:
                return None

        return recursion(root)
