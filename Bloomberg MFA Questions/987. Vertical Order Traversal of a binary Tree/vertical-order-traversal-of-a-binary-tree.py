import bisect
from typing import Optional, List
from collections import OrderedDict, deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([(root, 0, 0)])
        column_table = defaultdict(list)
        min_column = 0
        max_column = 0

        while queue:
            node, row_idx, column_idx = queue.popleft()

            if node:
                column_vals = column_table[column_idx]

                if column_vals:
                    peek_val = column_vals[len(column_vals) - 1][0]
                    peek_row = column_vals[len(column_vals) - 1][1]
                    peek_index = column_vals.index(
                        column_vals[len(column_vals) - 1])

                if column_vals and peek_row == row_idx and node.val < peek_val:
                    column_vals.insert(peek_index, (node.val, row_idx))
                else:
                    column_table[column_idx].append((node.val, row_idx))

                min_column = min(min_column, column_idx)
                max_column = max(max_column, column_idx)

            if node.left:
                queue.append((node.left, row_idx + 1, column_idx - 1))
            if node.right:
                queue.append((node.right, row_idx + 1, column_idx + 1))

        order = []
        for i in range(min_column, max_column + 1):
            temp = []
            for val, _ in column_table[i]:
                temp.append(val)
            order.append(temp)

        return order


class Solution2:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([(root, 0, 0)])
        column_table = defaultdict(list)
        min_column = 0
        max_column = 0

        while queue:
            node, row_idx, column_idx = queue.popleft()

            column_table[column_idx].append((row_idx, node.val))
            min_column = min(min_column, column_idx)
            max_column = max(max_column, column_idx)

            if node.left:
                queue.append((node.left, row_idx + 1, column_idx - 1))
            if node.right:
                queue.append((node.right, row_idx + 1, column_idx + 1))

        order = []
        for i in range(min_column, max_column + 1):
            order.append([val for _, val in sorted(column_table[i])])

        return order


class Solution3:
    # O(Nlog(N)) time | O(N) space
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([(root, 0, 0)])
        node_list = []

        while queue:
            node, row_idx, column_idx = queue.popleft()

            if node:
                node_list.append((column_idx, row_idx, node.val))

            if node.left:
                queue.append((node.left, row_idx + 1, column_idx - 1))
            if node.right:
                queue.append((node.right, row_idx + 1, column_idx + 1))

        node_list.sort()

        ordered_tree = {}
        for column, row, value in node_list:
            if column in ordered_tree:
                ordered_tree[column].append(value)
            else:
                ordered_tree[column] = [value]

        return list(ordered_tree.values())


class Solution4:
    # O(Nlog(N/K)) time | O(N) space - where "K" is the width of the tree and also the number
    # of columns
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0, 0)])
        column_table = defaultdict(list)
        min_column = 0
        max_column = 0

        while queue:
            node, row_idx, column_idx = queue.popleft()

            column_table[column_idx].append((row_idx, node.val))
            min_column = min(min_column, column_idx)
            max_column = max(max_column, column_idx)

            if node.left:
                queue.append((node.left, row_idx + 1, column_idx - 1))
            if node.right:
                queue.append((node.right, row_idx + 1, column_idx + 1))

        order = []
        for i in range(min_column, max_column + 1):
            temp = []
            for _, val in sorted(column_table[i]):
                temp.append(val)
            # order.append([val for _, val in sorted(column_table[i])])
            order.append(temp)

        return order


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(5)

    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.right = TreeNode(9)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(2)

    # Big Tree #
    # left branch
    bigTree = TreeNode(0)
    bigTree.left = TreeNode(7)
    bigTree.left.right = TreeNode(10)
    bigTree.left.right.left = TreeNode(11)
    bigTree.left.right.left.left = TreeNode(13)
    # right branch
    bigTree.right = TreeNode(1)
    bigTree.right.left = TreeNode(2)
    bigTree.right.left.right = TreeNode(14)
    bigTree.right.left.left = TreeNode(3)
    bigTree.right.left.left.right = TreeNode(4)
    bigTree.right.left.left.right.left = TreeNode(12)
    bigTree.right.left.left.right.right = TreeNode(5)
    bigTree.right.left.left.right.right.right = TreeNode(9)
    bigTree.right.left.left.right.right.left = TreeNode(6)
    bigTree.right.left.left.right.right.left.left = TreeNode(8)

    tree2 = TreeNode(0)
    tree2.left = TreeNode(2)
    tree2.left.left = TreeNode(3)
    tree2.left.left.right = TreeNode(4)
    tree2.left.left.right.right = TreeNode(6)
    tree2.left.left.right.right.left = TreeNode(7)
    tree2.left.left.right.left = TreeNode(8)
    tree2.left.left.right.left.right = TreeNode(17)

    sol = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    sol4 = Solution4()

    print(sol.verticalTraversal(root))
    print(sol2.verticalTraversal(root))
    print(sol3.verticalTraversal(root))
    print(sol4.verticalTraversal(root))

    # print(sol.verticalTraversal(tree))
    # print(sol.verticalTraversal(bigTree))
    # print(sol.verticalTraversal(tree2))
