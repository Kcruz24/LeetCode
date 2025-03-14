
# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])

        levels = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            levels.append(level)

        return levels
