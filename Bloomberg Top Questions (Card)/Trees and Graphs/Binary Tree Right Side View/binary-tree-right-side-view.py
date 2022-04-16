from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) time | O(D) space - where 'D' is the tree diameter
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        next_level = [root]
        right_side = []

        while next_level:
            curr_level = next_level
            next_level = []

            while curr_level:
                node = curr_level.pop(0)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            right_side.append(node.val)

        return right_side


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)

    sol = Solution()

    print(sol.rightSideView(root))
