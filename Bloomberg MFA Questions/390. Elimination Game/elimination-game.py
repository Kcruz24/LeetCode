
'''
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# Solution from:
# https://leetcode.com/problems/elimination-game/discuss/552326/Python-greater-95-Time-O(logN)-and-Constant-Memory-Commented-and-Explained


class Solution:
    # O(log(N)) Time | O(1) Space
    def lastRemaining(self, n: int) -> int:
        forward = True   # flag for forward/backward elimination
        steps = 2    # elimination step/interval
        base = 0   # elimination base

        while n > 1:
            if forward or n % 2 == 1:
                base += steps // 2
            steps *= 2
            n = n // 2
            forward = not forward   # reverse the pass direction

        return base + 1


if __name__ == '__main__':
    sol = Solution()

    n = 9
    print(sol.lastRemaining(n))
