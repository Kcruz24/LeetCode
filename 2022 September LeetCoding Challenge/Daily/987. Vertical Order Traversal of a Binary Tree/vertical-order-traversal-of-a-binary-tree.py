# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(NLog(N)) Time | O(N) Space
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        column_map = defaultdict(list)

        max_column = float('-inf')
        min_column = float('inf')

        stack = [(root, 0, 0)]
        while stack:
            node, row, column = stack.pop()

            column_map[column].append((row, node.val))
            max_column = max(column, max_column)
            min_column = min(column, min_column)

            if node.left:
                stack.append((node.left, row + 1, column - 1))

            if node.right:
                stack.append((node.right, row + 1, column + 1))

        output = []
        for i in range(min_column, max_column + 1):
            temp = []
            for _, val in sorted(column_map[i]):
                temp.append(val)
            output.append(temp)

        return output
