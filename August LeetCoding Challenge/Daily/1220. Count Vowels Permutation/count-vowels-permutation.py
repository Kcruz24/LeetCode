class Solution:
    # O(N) Time | O(1) Space
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] * 5   # number of string end at character i, with i=[a, e, i, o, u]
        for i in range(1, n):
            a, e, i, o, u = dp
            dp[0] = (e + u + i) % MOD
            dp[1] = (a + i) % MOD
            dp[2] = (e + o) % MOD
            dp[3] = i % MOD
            dp[4] = (o + i) % MOD

        return sum(dp) % MOD


if __name__ == '__main__':
    sol = Solution()

    n = 5

    print(sol.countVowelPermutation(n))