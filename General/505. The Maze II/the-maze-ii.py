'''

maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]

start = [0,4]
destination = [4,4]

'''


from collections import deque
import heapq
from typing import List

# DFS - TLE
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        def dfs(start):
            offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            start_row, start_col = start

            for offset_row, offset_col in offsets:
                new_row = start_row + offset_row
                new_col = start_col + offset_col
                steps = 0

                while new_row >= 0 and new_col >= 0 and new_row < row_length and new_col < col_length and maze[new_row][new_col] == 0:
                    new_row += offset_row
                    new_col += offset_col
                    steps += 1

                if distance[start_row][start_col] + steps < distance[new_row - offset_row][new_col - offset_col]:
                    distance[new_row - offset_row][new_col - offset_col] = distance[start_row][start_col] + steps
                    new_start = [new_row - offset_row, new_col - offset_col]
                    dfs(new_start)

        row_length = len(maze)
        col_length = len(maze[0])

        distance = [[float('inf')] * col_length for _ in range(row_length)]
        distance[start[0]][start[1]] = 0

        dfs(start)

        dest_row, dest_col = destination
        if distance[dest_row][dest_col] == float('inf'):
            return -1

        shortest_distance = distance[dest_row][dest_col]
        return shortest_distance


# BFS - Accepted
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        def bfs(start):
            queue = deque([start])
            offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]

            while queue:
                row, col = queue.popleft()

                for offset_row, offset_col in offsets:
                    new_row = row + offset_row
                    new_col = col + offset_col
                    steps = 0

                    while new_row >= 0 and new_col >= 0 and new_row < row_length and new_col < col_length and maze[new_row][new_col] == 0:
                        new_row += offset_row
                        new_col += offset_col
                        steps += 1

                    if distance[row][col] + steps < distance[new_row - offset_row][new_col - offset_col]:
                        distance[new_row - offset_row][new_col -
                                                       offset_col] = distance[row][col] + steps

                        new_start = [new_row - offset_row,
                                     new_col - offset_col]
                        queue.append(new_start)

        row_length = len(maze)
        col_length = len(maze[0])

        distance = [[float('inf')] * col_length for _ in range(row_length)]
        distance[start[0]][start[1]] = 0

        bfs(start)

        dest_row, dest_col = destination
        if distance[dest_row][dest_col] == float('inf'):
            return -1

        shortest_distance = distance[dest_row][dest_col]
        return shortest_distance


# Dijkstras - TLE
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        def min_distance():
            min = [-1, -1]
            min_val = float('inf')

            for row in range(len(distance)):
                for col in range(len(distance[0])):
                    if not visited[row][col] and distance[row][col] < min_val:
                        min[0] = row
                        min[1] = col
                        min_val = distance[row][col]

            return min

        def dijkstras():
            offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]

            while True:
                row, col = min_distance()

                if row < 0:
                    break

                visited[row][col] = True
                for offset_row, offset_col in offsets:
                    new_row = row + offset_row
                    new_col = col + offset_col
                    steps = 0

                    while new_row >= 0 and new_col >= 0 and new_row < row_length and new_col < col_length and maze[new_row][new_col] == 0:
                        new_row += offset_row
                        new_col += offset_col
                        steps += 1

                    if distance[row][col] + steps < distance[new_row - offset_row][new_col - offset_col]:
                        distance[new_row - offset_row][new_col -
                                                       offset_col] = distance[row][col] + steps

        row_length = len(maze)
        col_length = len(maze[0])

        distance = [[float('inf')] * col_length for _ in range(row_length)]
        distance[start[0]][start[1]] = 0

        visited = [[False] * col_length for _ in range(row_length)]

        dijkstras()

        dest_row, dest_col = destination
        if distance[dest_row][dest_col] == float('inf'):
            return -1

        shortest_distance = distance[dest_row][dest_col]
        return shortest_distance


# O(M*N * log(M*N)) Time | O(M*N) Space
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        def dijkstras():
            offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            pq = [(0, start[0], start[1])]

            while pq:
                curr_steps, row, col = heapq.heappop(pq)

                if distance[row][col] < curr_steps:
                    continue

                for offset_row, offset_col in offsets:
                    new_row = row + offset_row
                    new_col = col + offset_col
                    steps = 0

                    while new_row >= 0 and new_col >= 0 and new_row < row_length and new_col < col_length and maze[new_row][new_col] == 0:
                        new_row += offset_row
                        new_col += offset_col
                        steps += 1

                    prev_row = new_row - offset_row
                    prev_col = new_col - offset_col

                    if distance[row][col] + steps < distance[prev_row][prev_col]:

                        distance[prev_row][prev_col] = distance[row][col] + steps
                        new_step = distance[prev_row][prev_col]

                        heapq.heappush(pq, (new_step, prev_row, prev_col))

        row_length = len(maze)
        col_length = len(maze[0])

        distance = [[float('inf')] * col_length for _ in range(row_length)]
        distance[start[0]][start[1]] = 0

        dijkstras()

        dest_row, dest_col = destination
        if distance[dest_row][dest_col] == float('inf'):
            return -1

        shortest_distance = distance[dest_row][dest_col]
        return shortest_distance


if __name__ == '__main__':
    sol = Solution()

    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]

    start = [0, 4]
    destination = [4, 4]
    print(sol.shortestDistance(maze, start, destination))

    maze = [[0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0]]

    start = [0, 0]
    destination = [8, 6]
    print(sol.shortestDistance(maze, start, destination))
