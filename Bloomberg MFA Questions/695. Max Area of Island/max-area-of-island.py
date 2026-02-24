from typing import List


class Solution:
    # O(N*M) Time | O(N*M) Space
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def get_island_size(row, col):
            is_row_out_bounds = row < 0 or row >= row_length
            is_col_out_bounds = col < 0 or col >= col_length
            is_out_bounds = is_row_out_bounds or is_col_out_bounds

            if is_out_bounds:
                return 0

            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return 1 + get_island_size(row + 1, col) + \
                get_island_size(row - 1, col) + \
                get_island_size(row, col + 1) + \
                get_island_size(row, col - 1)

        row_length = len(grid)
        col_length = len(grid[0])
        max_area = 0

        for row in range(row_length):
            for col in range(col_length):
                if grid[row][col] == 1:
                    curr_island_size = get_island_size(row, col)
                    max_area = max(max_area, curr_island_size)

        return max_area
