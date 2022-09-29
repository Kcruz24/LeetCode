'''


'''

from typing import List
from collections import defaultdict


class Solution:
    # O(N) Time | O(N) Space
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        restricted = set(restricted)

        for a, b in edges:
            if a in restricted or b in restricted:
                continue

            graph[a].append(b)
            graph[b].append(a)

        visited = set([0])
        res = 1

        stack = [0]
        while stack:
            node = stack.pop()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    res += 1
                    visited.add(neighbor)
                    stack.append(neighbor)

        return res


class UnioFind:
    def __init__(self, n):
        self.roots = [node for node in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x == self.roots[x]:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.roots[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.roots[root_x] = root_y
            else:
                self.roots[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)