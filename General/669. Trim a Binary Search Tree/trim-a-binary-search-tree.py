from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.trim(root, high, low)

    def trim(self, root, low, high):
        if root is None:
            return

        if root.val > high:
            return self.trim(root.left, low, high)
        elif root.val < low:
            return self.trim(root.right, low, high)
        else:
            root.left = self.trim(root.left, low, high)
            root.right = self.trim(root.right, low, high)
            return root
