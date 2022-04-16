from typing import List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Does not work
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        queue = deque([target])
        depth = 0
        nodes_distance_k = []

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if depth == k:
                    nodes_distance_k.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return nodes_distance_k

# Solution
class Solution2:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        self.get_parents(root, None)

        result = []
        queue = deque([(target, 0)])
        visited = set()

        while queue:
            node, depth = queue.popleft()

            if node not in visited:
                if depth == k:
                    result.append(node.val)

                visited.add(node)

                if node.left:
                    queue.append((node.left, depth + 1))

                if node.right:
                    queue.append((node.right, depth + 1))

                if parents[node.val]:
                    parent = self.parents[node.val]

                    queue.append((parent, depth + 1))

        return result

    def get_parents(self, node, parent):
        if node is None:
            return

        self.parents[node.val] = parent

        self.get_parents(node.left, node)
        self.get_parents(node.right, node)


if __name__ == '__main__':
    sol = Solution2()

    root = TreeNode(3)

    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(8)

    solution = sol.distanceK(root, root.left, 2)

    parents = {}

    sol.get_parents(root, None, parents)

   # print(parents)

    print(parents[1].val)

    for k, v in parents.items():
        print(k, ':', v)

    #print(solution)
