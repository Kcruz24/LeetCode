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
        if not root:
            return 0

        stack = [(root, 1)]
        longest = 1

        while stack:
            node, path = stack.pop()
            longest = max(longest, path)

            if node.left:

                if node.left.val - node.val == 1:
                    stack.append((node.left, path + 1))
                else:
                    stack.append((node.left, 1))

            if node.right:

                if node.right.val - node.val == 1:
                    stack.append((node.right, path + 1))
                else:
                    stack.append((node.right, 1))

        return longest
