# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(N) Time | O(N) Space
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def sum_nodes(node):
            if not node:
                return 0

            left_sum = sum_nodes(node.left)
            right_sum = sum_nodes(node.right)
            subtree_sum = node.val + left_sum + right_sum
            all_subtrees.append(subtree_sum)

            return subtree_sum

        all_subtrees = []
        total_sum = sum_nodes(root)
        best_product = 0

        for subtree in all_subtrees:
            product = (total_sum - subtree) * subtree
            best_product = max(best_product, product)

        MOD = (10**9 + 7)
        return best_product % MOD
