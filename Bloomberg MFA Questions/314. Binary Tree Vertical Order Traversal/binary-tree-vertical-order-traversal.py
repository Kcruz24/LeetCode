from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(Nlog(N)) time | O(N) space
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = [(root, 0)]
        column_table = defaultdict(list)

        while queue:
            node, column_idx = queue.pop(0)
            column_table[column_idx].append(node.val)

            if node.left:
                queue.append((node.left, column_idx - 1))

            if node.right:
                queue.append((node.right, column_idx + 1))

        sort_keys = sorted(column_table.keys())
        order = []

        for key in sort_keys:
            order.append(column_table[key])

        return order


class LinearSolution:
    # O(N) time | O(N) space
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = [(root, 0)]
        order = []
        column_table = defaultdict(list)
        min_column_idx = 0
        max_column_idx = 0

        while queue:
            node, column_idx = queue.pop(0)

            if node:
                column_table[column_idx].append(node.val)
                min_column_idx = min(min_column_idx, column_idx)
                max_column_idx = max(max_column_idx, column_idx)

            if node.left:
                queue.append((node.left, column_idx - 1))

            if node.right:
                queue.append((node.right, column_idx + 1))

        # for node in range(min_column_idx, max_column_idx + 1):
        #     order.append(column_table[node])

        return [column_table[node] for node in range(min_column_idx, max_column_idx + 1)]

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(11)
    root.right = TreeNode(8)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(1)
    root.right.left.right = TreeNode(5)

    sol = Solution()
    sol2 = LinearSolution()

    print(sol.verticalOrder(root))
    print("\nLinear Solution")
    print(sol2.verticalOrder(root))

