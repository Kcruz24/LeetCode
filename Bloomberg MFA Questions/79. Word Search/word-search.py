from typing import List


# O(N*M + SP * 3^L) Time | O(L) Space - Where "L" is the length of the word to
# be matched. and "SP" are the starting positions found.
class Solution:
    # O(M*N) Time | O(1) Space
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row_length = len(board)
        self.col_length = len(board[0])

        starting_positions = []

        for row in range(self.row_length):
            for col in range(self.col_length):
                if board[row][col] == word[0]:
                    starting_positions.append((row, col))

        for row, col in starting_positions:
            if self.backtrack(row, col, word, board):
                return True

        return False

    # O(3^L) Time | O(L) Space - Where "L" is the length of the word to be
    # matched.
    def backtrack(self, row, col, word, board):
        if len(word) == 0:
            return True

        is_row_out_of_bounds = row < 0 or row == self.row_length
        is_col_out_of_bounds = col < 0 or col == self.col_length

        if is_row_out_of_bounds or is_col_out_of_bounds or board[row][col] != word[0]:
            return False

        board[row][col] = '#'
        result = False
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for row_offset, col_offset in offsets:
            new_row = row_offset + row
            new_col = col_offset + col
            sliced_word = word[1:]

            if self.bactrack(new_row, new_col, sliced_word, board):
                result = True

            if result:
                break

        board[row][col] = word[0]

        return result
