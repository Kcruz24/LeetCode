from collections import defaultdict
import heapq
from typing import List


class Solution:
    # O(NMlog(min(N,M))) Time | O(MN) Space
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row_length = len(mat)
        col_length = len(mat[0])

        diagonals = defaultdict(list)

        for row in range(row_length):
            for col in range(col_length):
                diagonals[row - col].append(mat[row][col])

        for diagonal in diagonals.values():
            heapq.heapify(diagonal)

        for row in range(row_length):
            for col in range(col_length):
                value = heapq.heappop(diagonals[row - col])
                mat[row][col] = value

        return mat


if __name__ == '__main__':
    sol = Solution()

    mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
    print(sol.diagonalSort(mat))
