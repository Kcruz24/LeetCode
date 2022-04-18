from collections import Counter

# Brute Force


class Solution1:
    # O(N^2) time | O(1) space
    def minSteps(self, s: str, t: str) -> int:
        for char in s:
            t = t.replace(char, '', 1)

        return len(t)

# Optimal


class Solution2:
    # O(N) time | O(1) space
    def minSteps(self, s: str, t: str) -> int:
        s_freq = Counter(s)
        steps = 0

        for char in t:
            if s_freq[char] > 0:
                s_freq[char] -= 1
            else:
                steps += 1

        return steps


if __name__ == '__main__':
    sol = Solution2()

    s = 'leetcode'
    t = 'practice'

    print(sol.minSteps(s, t))
