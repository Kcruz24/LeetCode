# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) Time | O(N) Space
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def longest_path(root):
            nonlocal maxval
            if not root:
                return [0, 0]

            inc = 1
            dcr = 1

            if root.left:
                left = longest_path(root.left)
                if root.val == root.left.val + 1:
                    dcr = left[1] + 1
                elif root.val == root.left.val - 1:
                    inc = left[0] + 1

            if root.right:
                right = longest_path(root.right)
                if root.val == root.right.val + 1:
                    dcr = max(dcr, right[1] + 1)
                elif root.val == root.right.val - 1:
                    inc = max(inc, right[0] + 1)

            maxval = max(maxval, dcr + inc - 1)
            return [inc, dcr]

        maxval = 0
        longest_path(root)
        return maxval
