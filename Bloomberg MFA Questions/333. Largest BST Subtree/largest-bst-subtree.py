# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N^3) Time | O(N) Space
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        max_val = float('inf')
        min_val = float('-inf')

        max_bst = 0
        stack = [root]
        while stack:
            node = stack.pop()
            bst_size = 0

            if self.is_valid_bst(node, min_val, max_val):
                bst_size = self.get_bst_size(node)
                max_bst = max(bst_size, max_bst)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return max_bst

    def get_bst_size(self, root):
        if not root:
            return 0

        return 1 + self.get_bst_size(root.left) + self.get_bst_size(root.right)

    def is_valid_bst(self, root, min, max):
        if root is None:
            return True

        if min >= root.val or root.val >= max:
            return False

        left = self.is_valid_bst(root.left, min, root.val)
        right = self.is_valid_bst(root.right, root.val, max)

        return left and right
