from typing import List


class Solution:
    # O(NLog(N)) Time | O(1) Space
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key=lambda x: x[0] - x[1])

        half = len(costs) // 2

        min_cost = 0
        city_a = 0
        city_b = 0

        for i in range(half):
            city_a = costs[i][0]
            city_b = costs[i + half][1]

        min_cost += city_a + city_b

        return min_cost


if __name__ == '__main__':
    sol = Solution()

    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    costs2 = [[259, 770], [448, 54], [926, 667],
              [184, 139], [840, 118], [577, 469]]

    print(sol.twoCitySchedCost(costs))

    print(sol.twoCitySchedCost(costs2))
