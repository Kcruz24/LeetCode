class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = (curr_number << 1) | root.val

                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))  # type: ignore
                    stack.append((root.left, curr_number))  # type: ignore

        return root_to_leaf
