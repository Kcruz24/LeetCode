# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def populate_parents(node, parent):
            if not node:
                return

            parents[node.val] = parent
            populate_parents(node.left, node)
            populate_parents(node.right, node)

        def get_node_from_parent(value):
            parent = parents[value]

            if not parent:
                return root

            if parent.left and parent.left.val == value:
                return parent.left

            return parent.right

        parents = {}
        populate_parents(root, None)

        start_node = get_node_from_parent(startValue)

        queue = deque([(start_node, '')])
        visited = set()

        while queue:
            node, dire = queue.popleft()

            visited.add(node)
            if node.val == destValue:
                return dire

            if parents[node.val] and parents[node.val] not in visited:
                queue.append((parents[node.val], dire + 'U'))

            if node.right and node.right not in visited:
                queue.append((node.right, dire + 'R'))

            if node.left and node.left not in visited:
                queue.append((node.left, dire + 'L'))

        return ''
