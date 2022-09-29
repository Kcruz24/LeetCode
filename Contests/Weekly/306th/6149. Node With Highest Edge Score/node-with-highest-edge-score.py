from os import dup
from typing import List
from collections import defaultdict, Counter


class Solution:
    # O(N) Time | O(N) Space
    def edgeScore(self, edges: List[int]) -> int:
        scores = defaultdict(int)

        for node, neighbor in enumerate(edges):
            scores[neighbor] += node

        max_score = max(scores.values())
        for i in range(len(edges)):
            if scores[i] == max_score:
                return i


if __name__ == '__main__':
    sol = Solution()

    edges = [1, 0, 0, 0, 0, 7, 7, 5]

    print(sol.edgeScore(edges))

    edges = [2, 0, 0, 1]

    print(sol.edgeScore(edges) == 0)

    edges = [2, 0, 0, 2]

    print(sol.edgeScore(edges) == 0)