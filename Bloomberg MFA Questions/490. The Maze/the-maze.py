from typing import List


class Solution:
    # O(M*N) Time | O(M+N) Space
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        def dfs(row, col):
            if (row, col) in visited:
                return False

            if (row, col) == (dest_row, dest_col):
                return True

            visited.add((row, col))

            right = col + 1
            left = col - 1
            up = row - 1
            down = row + 1

            while right < col_length and maze[row][right] == 0:  # RIGHT
                right += 1

            if dfs(row, right - 1):
                return True

            while left >= 0 and maze[row][left] == 0:  # LEFT
                left -= 1

            if dfs(row, left + 1):
                return True

            while up >= 0 and maze[up][col] == 0:  # UP
                up -= 1

            if dfs(up + 1, col):
                return True

            while down < row_length and maze[down][col] == 0:  # DOWN
                down += 1

            if dfs(down - 1, col):
                return True

            return False


        visited = set()

        row_length = len(maze)
        col_length = len(maze[0])

        start_row, start_col = start
        dest_row, dest_col = destination

        return dfs(start_row, start_col)



class Solution:
    # O(NxM) Time | O(NxM) Space
    def hasPath(self, maze, start, destination):

        def dfs(row, col):
            if [row, col] == destination:
                return True

            if (row, col) in visited:
                return False

            visited.add((row, col))

            neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for nei_row, nei_col in neighbors:
                new_row = row
                new_col = col

                while 0 <= new_row + nei_row < row_length and 0 <= new_col + nei_col < col_length and maze[new_row + nei_row][new_col + nei_col] == 0:
                    new_row += nei_row
                    new_col += nei_col

                if dfs(new_row, new_col):
                    return True

            return False

        row_length = len(maze)
        col_length = len(maze[0])

        visited = set()

        start_row, start_col = start

        return dfs(start_row, start_col)




if __name__ == '__main__':
    sol = Solution()

    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    destination = [4,4]
    print(sol.hasPath(maze, start, destination) == True)


    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    destination = [3,2]
    print(sol.hasPath(maze, start, destination) == False)

    maze = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
    start = [0, 0]
    destination = [8, 6]
    print(sol.hasPath(maze, start, destination) == True)

    maze = [[0,0,0],[0,0,0],[0,0,0]]
    start = [0,0]
    destination = [2,2]
    print(sol.hasPath(maze, start, destination) == True)


    maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
    start = [4,3]
    destination = [0,1]