from typing import List
from collections import Counter, defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        output = []
        counter = 1

        for node in range(n):
            start_node = edges[node][0]
            end_node = edges[node][1]

            if labels[start_node] == labels[end_node]:
                counter += 1

            # run recursive dfs

            output.append(counter)

        return output


class Solution2:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        def dfs(node: int):
            cnt = Counter()
            if node not in seen:
                cnt[labels[node]] += 1
                seen.add(node)
                for child in graph[node]:
                    cnt += dfs(child)
                ans[node] = cnt[labels[node]]
            return cnt

        graph = defaultdict(list)
        ans = [0] * n
        seen = set()

        for e, v in edges:
            graph[e] += [v]
            graph[v] += [e]

        dfs(0)
        return ans


if __name__ == '__main__':
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    labels = "abaedcd"

    sol2 = Solution2()
    print(sol2.countSubTrees(n, edges, labels))
