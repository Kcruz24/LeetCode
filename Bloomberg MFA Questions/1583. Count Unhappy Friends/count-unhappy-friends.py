from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        dd = {}

        for i, x in pairs:
            dd[i] = preferences[i][:preferences[i].index(x)]
            dd[x] = preferences[x][:preferences[x].index(i)]

        ans = 0

        for i in dd:
            for x in dd[i]:
                if i in dd[x]:
                    ans += 1
                    break

        return ans


class Solution2:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        likemore = {}
        for a, b in pairs:
            likemore[a] = set(preferences[a][:preferences[a].index(b)])
            likemore[b] = set(preferences[b][:preferences[b].index(a)])

        unhappy = set()
        for i in range(n):
            for j in range(i):
                if(i in likemore[j] and j in likemore[i]):
                    unhappy.add(i)
                    unhappy.add(j)
        return len(unhappy)


if __name__ == '__main__':
    sol = Solution2()

    n = 4
    preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    pairs = [[0, 1], [2, 3]]

    # Output should be 2
    print(sol.unhappyFriends(n, preferences, pairs))