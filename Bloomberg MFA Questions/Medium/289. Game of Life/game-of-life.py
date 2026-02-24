'''

- live cell with less than 2 live neighbors = dies (under population)
- live cell with 2 or 3 live neighbors = lives (next gen)
- live cell with more than 3 live neighbors = dies (Over population)
- dead cell with exactly 3 live neighbors = comes back to life (reproduction)

'''

from typing import List
from copy import deepcopy


class Solution:
    # O(N*M) Time | O(N*M) Space
    def gameOfLife(self, board: List[List[int]]):
        copy_board = deepcopy(board)

        row_length = len(board)
        col_length = len(board[0])

        for row in range(row_length):
            for col in range(col_length):
                neighbors = get_neighbors(row, col, board)

                live_neighbors = 0
                for neighbor in neighbors:
                    n_row, n_col = neighbor

                    if copy_board[n_row][n_col] == 1:
                        live_neighbors += 1

                live_cell = copy_board[row][col] == 1
                under_population = live_neighbors < 2
                over_population = live_neighbors > 3
                reproduction = live_neighbors == 3
                next_generation = live_neighbors == 2 or live_neighbors == 3

                if live_cell and next_generation:
                    continue

                if live_cell and under_population or over_population:
                    board[row][col] = 0
                elif reproduction:
                    board[row][col] = 1

        return board


class Solution2:
    # O(N*M) Time | O(1) Space
    def gameOfLife(self, board: List[List[int]]) -> None:
        row_length = len(board)
        col_length = len(board[0])

        for row in range(row_length):
            for col in range(col_length):
                neighbors = get_neighbors(row, col, board)

                live_neighbors = 0
                for neighbor_row, neighbor_col in neighbors:

                    is_live_neighbor = abs(
                        board[neighbor_row][neighbor_col]) == 1
                    if is_live_neighbor:
                        live_neighbors += 1

                live_cell = board[row][col] == 1

                # Rules
                under_population = live_neighbors < 2
                over_population = live_neighbors > 3
                reproduction = live_neighbors == 3
                next_generation = live_neighbors == 2 or live_neighbors == 3

                # Rule 2
                if live_cell and next_generation:
                    continue

                if live_cell:
                    # Rule 1 and 3
                    if under_population or over_population:
                        board[row][col] = -1

                # Rule 4
                elif reproduction:
                    board[row][col] = 2

        # Update board with next state (final values)
        for row in range(row_length):
            for col in range(col_length):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


def get_neighbors(row, col, board):
    neighbors = []
    row_length = len(board)
    col_length = len(board[0])

    down = row + 1 < row_length
    up = row - 1 >= 0
    right = col + 1 < col_length
    left = col - 1 >= 0

    # ADJACENT NEIGHBORS
    if down:
        neighbors.append((row + 1, col))
    if up:
        neighbors.append((row - 1, col))
    if right:
        neighbors.append((row, col + 1))
    if left:
        neighbors.append((row, col - 1))

    # DIAGONAL NEIGHBORS
    if up and right:
        neighbors.append((row - 1, col + 1))
    if up and left:
        neighbors.append((row - 1, col - 1))
    if down and right:
        neighbors.append((row + 1, col + 1))
    if down and left:
        neighbors.append((row + 1, col - 1))

    return neighbors


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()

    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print(sol.gameOfLife(board))

    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print(sol2.gameOfLife(board))

    #board = [[1, 1], [1, 0]]
    #print(sol.gameOfLife(board))
