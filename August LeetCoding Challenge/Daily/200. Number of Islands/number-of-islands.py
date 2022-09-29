from typing import List


class Solution:
    # O(NxM) Time | O(NxM) Space
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            is_row_out_of_bounds = row < 0 or row >= row_length
            is_col_out_of_bounds = col < 0 or col >= col_length
            is_out_of_bounds = is_row_out_of_bounds or is_col_out_of_bounds

            if is_out_of_bounds:
                return

            if seen[row][col] or grid[row][col] == '0':
                return

            seen[row][col] = True

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return

        row_length = len(grid)
        col_length = len(grid[0])

        islands = 0
        seen = [[False] * col_length for _ in range(row_length)]

        for row in range(row_length):
            for col in range(col_length):
                if grid[row][col] == '1' and not seen[row][col]:
                    dfs(row, col)
                    islands += 1

        return islands
