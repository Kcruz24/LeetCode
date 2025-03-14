# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) Time | O(N) Space
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def contains_one(node):
            if not node:
                return False

            if node.val == 1:
                return True

            left_tree = contains_one(node.left)
            right_tree = contains_one(node.right)

            return left_tree or right_tree


        def dfs(node):
            if not node:
                return

            if not contains_one(node.left):
                node.left = None

            if not contains_one(node.right):
                node.right = None

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        if not root.left and not root.right and root.val == 0:
            return None

        return root


class Solution:
    # O(N) Time | O(N) Space
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def check_and_prune(node):
            if not node:
                return None

            node.left = check_and_prune(node.left)
            node.right = check_and_prune(node.right)

            if node.val == 0 and node.left is None and node.right is None:
                return None
            else:
                return node

        return check_and_prune(root)


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)

    Solution().pruneTree(root)

    # print(sol)
