# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) Time | O(N) Space
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, path, remaining_sum):
            if not node:
                return

            path.append(node.val)
            if remaining_sum == node.val and node.right is None and node.left is None:
                all_paths.append(path.copy())

            dfs(node.left, path, remaining_sum - node.val)
            dfs(node.right, path, remaining_sum - node.val)

            path.pop()

        all_paths = []
        dfs(root, [], targetSum)

        return all_paths


if __name__ == '__main__':
    root = TreeNode(5)

    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    targetSum = 22

    sol = Solution()

    print(sol.pathSum(root, targetSum))
