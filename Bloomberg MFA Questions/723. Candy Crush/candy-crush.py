from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        todo = False

        # Check for horizontal crushables
        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = - \
                        abs(board[r][c])
                    todo = True

        # Check for vertical crushables
        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = - \
                        abs(board[r][c])
                    todo = True

        # Uncrushed candies fall into place
        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board

# From a guy on leetcode: @jkp5380


class Solution2:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        row_length, col_length = len(board), len(board[0])
        stable = False
        while True:
            stable = True
            crushable = set()
            # 1. check for horizontal crushables
            for row in range(row_length):
                for col in range(col_length-2):
                    if board[row][col] == board[row][col+1] == board[row][col+2] != 0:
                        stable = False
                        crushable.update(
                            [(row, col), (row, col+1), (row, col+2)])

            # 2. check for vertical crushables
            for row in range(row_length-2):
                for col in range(col_length):
                    if board[row][col] == board[row+1][col] == board[row+2][col] != 0:
                        stable = False
                        crushable.update(
                            [(row, col), (row+1, col), (row+2, col)])

            # 5. if no candies were crushed, we're done
            if stable:
                return board

            # 3. crush the candies
            for row, col in crushable:
                board[row][col] = 0

            # 4. let the candies "fall"
            for col in range(col_length):
                offset = 0
                for row in range(row_length-1, -1, -1):  # loop through column backward
                    k = row + offset
                    if (row, col) in crushable:  # this will help us put items at bottom of the board
                        offset += 1
                    else:
                        board[k][col] = board[row][col]  # notice the use of k
                # now that all items have been copied to their right spots, place zero's appropriately at the top of the board
                for row in range(offset):
                    board[row][col] = 0


class Solution3:
    # O((M * N)^2) time | O(N) space
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        row_length = len(board)
        col_length = len(board[0])

        while True:
            stable = True

            crushables = set()

            # Horizontal crushables
            for row in range(row_length):
                for col in range(col_length - 2):
                    if board[row][col] == board[row][col + 1] == board[row][col + 2] != 0:
                        stable = False
                        crushables.update(
                            [(row, col), (row, col + 1), (row, col + 2)])

            # Vertical crushables
            for row in range(row_length - 2):
                for col in range(col_length):
                    if board[row][col] == board[row + 1][col] == board[row + 2][col] != 0:
                        stable = False
                        crushables.update(
                            [(row, col), (row + 1, col), (row + 2, col)])

            if stable:
                return board

            # Crush elements
            for row, col in crushables:
                board[row][col] = 0

            # Drop elements
            for col in range(col_length):
                offset = 0
                for row in reversed(range(row_length)):
                    if (row, col) in crushables:
                        offset += 1
                        continue

                    board[offset + row][col] = board[row][col]

                for row_top in range(offset):
                    board[row_top][col] = 0



#https://leetcode.com/problems/candy-crush/discuss/1028524/Python-Straightforward-and-Clean-with-Explanation
if __name__ == '__main__':
    board = [
        [110, 5, 112, 113, 114],
        [210, 211, 5, 213, 214],
        [310, 311, 3, 313, 314],
        [410, 411, 412, 5, 414],
        [5, 1, 512, 3, 3],
        [610, 4, 1, 613, 614],
        [710, 1, 2, 713, 714],
        [810, 1, 2, 1, 1],
        [1, 1, 2, 2, 2],
        [4, 1, 4, 4, 1014]
    ]

    sol = Solution3()

    print(sol.candyCrush(board))
