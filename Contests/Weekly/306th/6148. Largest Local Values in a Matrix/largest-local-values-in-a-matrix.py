from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        local_values = []
        row_length = len(grid)
        col_length = len(grid[0])
        temp = []

        row_start = 0
        col_start = 0
        row_end = 3
        col_end = 3

        flag = True
        while flag:

            max_local = float('-inf')
            for row in range(row_start, row_end):
                for col in range(col_start, col_end):
                    max_local = max(max_local, grid[row][col])
                    if (row, col) == (row_length - 1, col_length - 1):
                        flag = False

            temp.append(max_local)
            if col_end == col_length:
                row_start += 1
                col_start = 0
                row_end += 1
                col_end = 3
                local_values.append(temp.copy())
                temp.clear()
            else:
                col_start += 1
                col_end += 1

        return local_values


class Solution2:
    def largestLocal(self, grid):
        n = len(grid)
        local_values = []

        for row in range(n - 2):
            local_values.append([])
            for col in range(n - 2):
                row_one = max(grid[row][col : col + 3])
                row_two = max(grid[row + 1][col : col + 3])
                row_three = max(grid[row + 2][col : col + 3])

                max_local = max(row_one, row_two, row_three)
                local_values[row].append(max_local)

        return local_values

if __name__ == '__main__':
    sol = Solution()

    grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

    print(sol.largestLocal(grid))