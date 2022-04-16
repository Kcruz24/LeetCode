from collections import deque, defaultdict
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    if root is None:
        return

    queue = deque([root])
    zigzag_hashmap = defaultdict(deque)
    level = 0

    while queue:

        for _ in range(len(queue)):
            node = queue.popleft()

            if level % 2 == 0:
                zigzag_hashmap[level].append(node.val)
            else:
                zigzag_hashmap[level].appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

    return list(zigzag_hashmap.values())

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(zigzag_level_order(root))