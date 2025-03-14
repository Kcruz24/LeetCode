# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) Time | O(N) Space
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ''

            if node.left is None and node.right is None:
                return str(node.val) + ''

            if node.right is None:
                return str(node.val) + '(' + dfs(node.left) + ')'

            return str(node.val) + '(' + dfs(node.left) + ')(' + dfs(node.right) + ')'

        return dfs(root)


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        if not root.left and not root.right:
            return str(root.val)

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        return f'{root.val}({left})' + (f'({right})' if right else '')


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    sol = Solution().tree2str(root)
    print(sol)
