from typing import List


class Solution:
    # O(MxN) time | O(MxN) space
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for col in grid[0]] for row in grid]
        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands += self.traverse_island(grid, visited, row, col)

        return islands

    def traverse_island(self, grid, visited, row, col):
        stack = [(row, col)]

        while len(stack) > 0:
            inner_row, inner_col = stack.pop()

            if visited[inner_row][inner_col]:
                continue

            visited[inner_row][inner_col] = True

            neighbors = self.get_neighbors(grid, inner_row, inner_col)
            for row, col in neighbors:
                if grid[row][col] == "1":
                    stack.append((row, col))

        return 1

    def get_neighbors(self, grid, row, col):
        neighbors = []
        last_row = len(grid)
        last_col = len(grid[0])

        if row - 1 >= 0:  # UP
            neighbors.append((row - 1, col))
        if row + 1 < last_row:  # DOWN
            neighbors.append((row + 1, col))
        if col - 1 >= 0:  # LEFT
            neighbors.append((row, col - 1))
        if col + 1 < last_col:  # RIGHT
            neighbors.append((row, col + 1))

        return neighbors
