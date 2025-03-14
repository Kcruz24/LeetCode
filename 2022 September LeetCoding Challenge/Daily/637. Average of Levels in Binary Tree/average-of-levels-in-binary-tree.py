from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) Time | O(N) Space
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfs():
            queue = deque([root])

            levels = []
            while queue:
                size = len(queue)
                level_total = 0
                for _ in range(size):
                    node = queue.popleft()

                    level_total += node.val

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                levels.append(level_total / size)

            return levels

        return bfs()