from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) time | O(N) space
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = []
        queue = deque([root])

        while queue:
            values = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                values.insert(0, node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)
            levels.append(values)

        bottom_order = []
        while levels:
            bottom_order.append(levels.pop())

        return bottom_order


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()

    print(sol.levelOrderBottom(root))

    arr = [3, 4, 5]
    extended_arr = [1, 2, *arr]
