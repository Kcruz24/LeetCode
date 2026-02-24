from collections import defaultdict
from typing import List


# Path Search in Graph
class Solution:
    # O(M*N) Time | O(N) Space
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def backtrack_evaluate(curr_node, target_node, product):
            visited.add(curr_node)
            ans = -1.0
            neighbors = graph[curr_node]

            if target_node in neighbors:
                ans = product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue

                    acum = product * value
                    ans = backtrack_evaluate(neighbor, target_node, acum)

                    if ans != -1.0:
                        break

            visited.remove(curr_node)
            return ans

        graph = defaultdict(defaultdict)

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        results = []
        ans = 0
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ans = -1.0
            elif dividend == divisor:
                ans = 1.0
            else:
                visited = set()
                ans = backtrack_evaluate(dividend, divisor, 1)
            results.append(ans)

        return results
