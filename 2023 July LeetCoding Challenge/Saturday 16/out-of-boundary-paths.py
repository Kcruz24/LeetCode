# Dynamic Programming
# The current solution is not following DP, but the optimal ones are in DP

class Solution:
    # Brute Force
    # O(4^N) Time | O(N) Space
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
            return 1

        if maxMove == 0:
            return 0

        return self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn) \
            + self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn) \
            + self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1) \
            + self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)


if __name__ == "__main__":
    sol = Solution()

    m = 1
    n = 3
    maxMove = 3
    startRow = 0
    startColumn = 1

    print(sol.findPaths(m, n, maxMove, startRow, startColumn))
