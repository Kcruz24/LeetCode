from typing import List


class Solution:
    # O(N) time | O(N) space
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        results = []
        current_path = [0]
        last_node = len(graph) - 1
        self.dfs(0, current_path, graph, results, last_node)
        return results

    def dfs(self, vertex: int, current_path: List[int], graph: List[List[int]], results: List[int], last_node: int):
        if vertex == last_node:
            results.append(list(current_path))
            return

        for child in graph[vertex]:
            current_path.append(child)
            self.dfs(child, current_path, graph, results, last_node)
            current_path.pop()
