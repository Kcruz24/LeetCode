from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(N) time | O(N) space
    def isSymmetric(self, root: Optional[TreeNode]):
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: TreeNode, right: TreeNode):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False

        outPair = self.isMirror(left.left, right.right)
        inPair = self.isMirror(left.right, right.left)
        return outPair and inPair

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    sol = Solution()

    print(sol.isSymmetric(root))