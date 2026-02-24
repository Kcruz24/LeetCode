'''

- For every node, check if it is a valid BST
- If it is a valid BST, we count the number of nodes
- Compare the number of nodes to the largest BST

'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DOES NOT WORK


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.largest_bst(root, float('-inf'))

    def largest_bst(self, root: Optional[TreeNode], largest):
        if root is None:
            return largest

        if self.is_valid_bst(root, float('-inf'), float('inf')):
            count = self.dfs(root, 0)
            if count > largest:
                largest = count

        self.largest_bst(root.left, largest)
        self.largest_bst(root.right, largest)

        return largest

    def is_valid_bst(self, root: Optional[TreeNode], smallest, largest):
        if root is None:
            return True

        if smallest > root.val or root.val >= largest:
            return False

        left_tree_is_valid = self.is_valid_bst(root.left, smallest, root.val)
        right_tree_is_valid = self.is_valid_bst(root.right, root.val, largest)

        return left_tree_is_valid and right_tree_is_valid

    def dfs(self, root: Optional[TreeNode], count):
        if root is None:
            return count

        count += 1

        self.dfs(root.left, count)
        self.dfs(root.right, count)

        return count
