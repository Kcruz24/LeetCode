from typing import List


class Solution:
    # O(Nlog(N)) Time | O(N) Space
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        ranks = []
        rank_map = {}
        rank = 1

        for i in sorted(arr):
            if i in rank_map:
                continue

            rank_map[i] = rank
            rank += 1

        for num in arr:
            ranks.append(rank_map[num])

        return ranks


if __name__ == '__main__':
    sol = Solution()

    arr = [40, 10, 20, 30]
    print(sol.arrayRankTransform(arr))

    arr = [100, 100, 100]
    print(sol.arrayRankTransform(arr))
