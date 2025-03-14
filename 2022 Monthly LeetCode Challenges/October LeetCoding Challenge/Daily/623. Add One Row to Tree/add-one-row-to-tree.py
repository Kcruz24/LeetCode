# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val, root)
            return new_root

        def insert(node):
            new_node_left = TreeNode(val)

            temp = node.left
            node.left = None

            node.left = new_node_left
            new_node_left.left = temp

            new_node_right = TreeNode(val)

            temp = node.right
            node.right = None

            node.right = new_node_right
            new_node_right.right = temp

        def dfs(node, running_depth):
            if not node:
                return 0

            if running_depth == depth - 1:
                insert(node)

            return running_depth + max(dfs(node.left, running_depth + 1), dfs(node.right, running_depth + 1))

        running_depth = 1
        dfs(root, running_depth)
        return root


def preorder(root, arr):
    if not root:
        return

    arr.append(root.val)
    preorder(root.left, arr)
    preorder(root.right, arr)

    return arr


if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)

    root.right = TreeNode(6)
    root.right.left = TreeNode(5)

    print(preorder(root, []))

    node = sol.addOneRow(root, 1, 2)

    print(preorder(node, []))

    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.right = TreeNode(1)
    root.left.left.left = TreeNode(3)

    root.right = TreeNode(1)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(5)

    print(preorder(root, []))

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)

    val = 1
    depth = 3

    node = sol.addOneRow(root, val, depth)

    print(preorder(node, []))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    val = 5
    depth = 4

    node = sol.addOneRow(root, val, depth)

    print(preorder(node, []))
