from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) time | O(N) space
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root.right is None and root.left is None:
            return [root.val]

        left_boundary = deque()
        if root.left:
            self.left_boundary(root, left_boundary)
            left_boundary.pop()
        else:
            left_boundary.append(root.val)

        bottom_boundary = deque()
        self.bottom_boundary(root, bottom_boundary)

        right_boundary = deque()
        self.right_boundary(root.right, bottom_boundary, right_boundary)
        if right_boundary:
            right_boundary.pop()

        boundary = deque([*left_boundary, *bottom_boundary])

        while right_boundary:
            boundary.append(right_boundary.pop())

        return list(boundary)

    def left_boundary(self, tree, boundary):
        if tree is None:
            return

        boundary.append(tree.val)

        self.left_boundary(tree.left, boundary)
        if tree.left is None:
            self.left_boundary(tree.right, boundary)

    def bottom_boundary(self, tree, boundary):
        if tree is None:
            return

        self.bottom_boundary(tree.left, boundary)
        self.bottom_boundary(tree.right, boundary)

        if tree.left is None and tree.right is None:
            boundary.append(tree.val)

    def right_boundary(self, tree, bottom_boundary, boundary):
        if tree is None:
            return

        if tree not in bottom_boundary:
            boundary.append(tree.val)

        self.right_boundary(tree.right, bottom_boundary, boundary)
        if tree.right is None:
            self.right_boundary(tree.left, bottom_boundary, boundary)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(10)
    root.right.left.left = TreeNode(9)

    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)

    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(4)

    root3 = TreeNode(0)
    root3.left = TreeNode(0)
    root3.left.left = TreeNode(0)
    root3.right = TreeNode(0)
    root3.right.right = TreeNode(0)
    root3.right.right.right = TreeNode(0)

    sol = Solution()

    r1 = [1, 2, 4, 7, 8, 9, 10, 6, 3]
    r2 = [1, 3, 4, 2]
    r3 = [0, 0, 0, 0, 0, 0]
    print('r1 =', sol.boundaryOfBinaryTree(root) == r1)
    print('r2 = ', sol.boundaryOfBinaryTree(root2) == r2)
    print('r3 = ', sol.boundaryOfBinaryTree(root3) == r3)
