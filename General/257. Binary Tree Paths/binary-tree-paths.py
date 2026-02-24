# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N^2) Time | O(N) Space
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))
            if node.right is None and node.left is None:
                all_paths.append('->'.join(path))

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        all_paths = []
        dfs(root, [])

        return all_paths
