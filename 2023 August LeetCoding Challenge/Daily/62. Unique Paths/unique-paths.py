class Solution:
    # TLE
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution2:
    # O(M * N) Time | O(M * N) Space
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * m for _ in range(n)]

        for row in range(1, n):
            for col in range(1, m):
                paths[row][col] = paths[row][col -1] + paths[row - 1][col]

        return paths[-1][-1]


class Solution3:
    # O(M * N) Time | O(min(M, N)) Space
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            n, m = m, n

        dp = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]

        return dp[-1]


if __name__ == '__main__':
    sol = Solution2()

    m = 3
    n = 7

    print(sol.uniquePaths(m, n))
