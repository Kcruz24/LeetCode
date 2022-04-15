
# Definition for a Node.
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.next = None



class Solution:
    # Not Optimal
    # O(N) time | O(N) space
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if not root:
            return root

        queue = deque([root])

        while queue:

            size = len(queue)

            for i in range(size):

                node = queue.popleft()

                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root



class Solution2:
    # Optimal
    # O(N) time | O(1) space
    def connect(self, root: Node) -> Node:
        head = root

        while head and head.left:
            left_most = head.left

            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left
                head = head.next

            head = left_most

        return root
