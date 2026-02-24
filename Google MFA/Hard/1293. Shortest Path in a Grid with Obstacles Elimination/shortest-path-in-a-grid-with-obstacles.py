from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        last_row = len(grid) - 1
        last_col = len(grid[0]) - 1
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        state = (0, 0, k)
        queue = deque([(state, 0)])

        seen = set(state)

        while queue:
            (curr_row, curr_col, curr_k), dist = queue.popleft()

            if (curr_row, curr_col) == (last_row, last_col):
                return dist

            neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for neighbor_row, neighbor_col in neighbors:
                new_row = neighbor_row + curr_row
                new_col = neighbor_col + curr_col

                is_row_out_of_bounds = new_row < 0 or new_row >= len(grid)
                is_col_out_of_bounds = new_col < 0 or new_col >= len(grid[0])
                is_out_of_bounds = is_row_out_of_bounds or is_col_out_of_bounds

                if is_out_of_bounds:
                    continue

                remove_obstacle = curr_k - grid[new_row][new_col]
                new_state = (new_row, new_col, remove_obstacle)

                if remove_obstacle >= 0 and new_state not in seen:
                    seen.add(new_state)
                    queue.append((new_state, dist + 1))

        return -1


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
    k = 1
    print(sol.shortestPath(grid, k))

    grid = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 0, 0]
    ]

    k = 1
    print(sol.shortestPath(grid, k))
