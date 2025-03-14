from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''

nums = [-10,-3,0,5,9]


- The middle is our root node
- Values at its left is the left subtree, values at its right is the right subtree
- Traverse them and add them to the tree structure.

'''
class Solution:
    # O(N) Time | O(log(N)) Space
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        last_idx = len(nums) -1
        start = 0

        return self.add_child(nums, start, last_idx)


    def add_child(self, nums, left, right):
        if left > right:
            return

        mid = (left + right) // 2

        root = TreeNode(nums[mid])

        root.left = self.add_child(nums, left, mid - 1)
        root.right = self.add_child(nums, mid + 1, right)

        return root
