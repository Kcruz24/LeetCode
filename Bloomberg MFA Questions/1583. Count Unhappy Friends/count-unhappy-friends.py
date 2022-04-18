from typing import List

# From: https://leetcode.com/problems/count-unhappy-friends/discuss/1890091/Python-Make-you-happy-with-clean-and-concise-solution
class Solution:
    # O(N^2) time | O(N^2) space
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # Map to get pair mapping
        pairMap = {}
        # To get preference of person i with person j in O(1)
        prefer = {}

        # Populating pairMap
        for p1, p2 in pairs:
            pairMap[p1] = p2
            pairMap[p2] = p1

        # Populating prefer Map
        for i in range(len(preferences)):
            for j in range(n-1):
                if i not in prefer:
                    prefer[i] = {}
                prefer[i][preferences[i][j]] = j

        # Looping through preferences again to find if person i is unhappy
        res = 0
        for i in range(len(preferences)):
            for j in range(n-1):
                x = i
                y = pairMap[x]
                u = preferences[x][j]
                v = pairMap[u]
                
                if prefer[x][u] < prefer[x][y] and prefer[u][x] < prefer[u][v]:
                    res += 1
                    break
        return res


if __name__ == '__main__':
    sol = Solution()

    n = 4
    preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    pairs = [[0, 1], [2, 3]]

    # Output should be 2
    print(sol.unhappyFriends(n, preferences, pairs))