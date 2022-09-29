# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        nodes_to_parents = {}
        self.populate_node_to_parents(root, nodes_to_parents)

        start_node = self.get_node(root, start, nodes_to_parents)
        queue = deque([start_node])
        seen = set([start])

        minutes = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_node = queue.popleft()

                neighbors = [curr_node.left, curr_node.right, nodes_to_parents[curr_node.val]]
                for neighbor in neighbors:
                    if neighbor and neighbor.val not in seen:
                        seen.add(neighbor.val)
                        queue.append(neighbor)

            if queue:
                minutes += 1

        return minutes


    def populate_node_to_parents(self, root, nodes_to_parents, parent=None):
        if root:
            nodes_to_parents[root.val] = parent
            self.populate_node_to_parents(root.left, nodes_to_parents, root)
            self.populate_node_to_parents(root.right, nodes_to_parents, root)


    def get_node(self, root, value, nodes_to_parents):
        if root.val == value:
            return root

        node_parent = nodes_to_parents[value]
        if node_parent.left and node_parent.left.val == value:
            return node_parent.left

        return node_parent.right


if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(1)
    # root.left = TreeNode(5)
    # root.right = TreeNode(3)
    # root.right.right = TreeNode(6)
    # root.right.left = TreeNode(10)
    # root.left.right = TreeNode(4)
    # root.left.right.right = TreeNode(2)
    # root.left.right.left = TreeNode(9)

    start = 1

    print(sol.amountOfTime(root, start))