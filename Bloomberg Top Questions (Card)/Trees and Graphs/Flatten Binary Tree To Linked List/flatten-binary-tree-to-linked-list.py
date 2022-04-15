# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(N) time | O(1) space
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Handle the null scenario
        if not root:
            return None

        node = root
        while node:

            # If the node has a left child
            if node.left:

                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # move on to the right side of the tree
            node = node.right


class Solution:
    # O(N) time | O(N) space
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            nodes = []
            self.get_nodes(root, nodes)

            for i in range(len(nodes) - 1):
                nodes[i].left = None
                nodes[i].right = nodes[i + 1]

            nodes[len(nodes) - 1].left = None

    # O(N) time | O(N) space
    def get_nodes(self, root, array=[]):
        if root is None:
            return

        array.append(root)
        self.get_nodes(root.left, array)
        self.get_nodes(root.right, array)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    sol = Solution()

    sol.flatten(root)

    trav = root
    while trav != None:
        print(trav.val)
        trav = trav.right
