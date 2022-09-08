from typing import List

'''

Steps:
    1. look for every element in the left and top border
    2. do a diagonal dfs for each element
    3. if an element is not equal during the diagonal dfs, we return False
    4. return True

'''


class Solution:
    # O(N*M) Time | O(N) Space
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_length = len(matrix)
        col_length = len(matrix[0])
        is_toeplitz = True

        for row in range(row_length):
            for col in range(col_length):
                left_border = row >= 0 and col == 0
                top_border = row == 0 and col >= 0
                is_border = left_border or top_border

                if is_border:
                    is_toeplitz = self.diagonal_dfs(row, col, matrix)

                if not is_toeplitz:
                    return False

        return is_toeplitz

    def diagonal_dfs(self, row, col, matrix):
        stack = [(row, col)]

        while stack:
            row, col = stack.pop()

            diagonal_neighbors = self.get_neighbors(row, col, matrix)
            for in_row, in_col in diagonal_neighbors:
                if matrix[row][col] != matrix[in_row][in_col]:
                    return False

                stack.append((in_row, in_col))

        return True

    def get_neighbors(self, row, col, matrix):
        row_length = len(matrix)
        col_length = len(matrix[0])

        neighbors = []

        down = row + 1 < row_length
        right = col + 1 < col_length

        if down and right:
            neighbors.append((row + 1, col + 1))

        return neighbors
