# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(N) Time | O(N) Space
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate_bst(root, float('-inf'), float('inf'))


    def validate_bst(self, root, min_val, max_val):
        if root is None:
            return True

        if min_val >= root.val or root.val >= max_val:
            return False

        left_subtree = self.validate_bst(root.left, min_val, root.val)
        right_subtree = self.validate_bst(root.right, root.val, max_val)

        return left_subtree and right_subtree
