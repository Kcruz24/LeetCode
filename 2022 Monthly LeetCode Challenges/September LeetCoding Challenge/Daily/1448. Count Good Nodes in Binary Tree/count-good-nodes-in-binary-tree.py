# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS (Iterative)
class Solution:
    # O(N) Time | O(N) Space
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0
        stack = [(root, float('-inf'))]

        while stack:
            root, min_val = stack.pop()

            if root.val >= min_val:
                min_val = root.val
                good_nodes += 1

            if root.right:
                stack.append((root.right, min_val))

            if root.left:
                stack.append((root.left, min_val))

        return good_nodes


# DFS (Recursive)
class Solution:
    # O(N) Time | O(N) Space
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_so_far):
            if not root:
                return

            nonlocal good_nodes
            if max_so_far <= root.val:
                good_nodes += 1

            max_val = max(max_so_far, root.val)
            dfs(root.left, max_val)
            dfs(root.right, max_val)

            return good_nodes

        good_nodes = 0
        return dfs(root, float('-inf'))