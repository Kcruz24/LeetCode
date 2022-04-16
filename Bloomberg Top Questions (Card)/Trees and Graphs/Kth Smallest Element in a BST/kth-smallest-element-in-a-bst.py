from typing import Optional

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    # O(N) time | O(N) space
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        self.getNodes(root, nodes)

        kthSmallestIdx = k - 1
        kthSmallestElement = nodes[kthSmallestIdx]

        return kthSmallestElement

    def getNodes(self, tree, array):
        if tree is None:
            return

        self.getNodes(tree.left, array)
        array.append(tree.val)
        self.getNodes(tree.right, array)
