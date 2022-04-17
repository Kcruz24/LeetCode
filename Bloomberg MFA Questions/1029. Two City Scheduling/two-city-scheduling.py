from typing import List


class Solution3:
    # O(NLog(N)) time | O(N) space
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        N = len(costs) // 2
        minCost = 0

        for A, B in costs:
            refund.append(B - A)
            minCost += A

        refund.sort()

        for i in range(N):
            minCost += refund[i]

        return minCost

class Solution2:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # first assume that everyone is going to city A
        # then identify N people to go to city B
        # according to how much they can help save when
        # changing destination
        # to city B
        N = len(costs)//2
        total_cost_A = 0
        d = []
        #
        for i in range(2*N):
            total_cost_A += costs[i][0]
            d.append(costs[i][0]-costs[i][1])
        # sort the difference (from large to small)
        d.sort(reverse=True)

        return(total_cost_A - sum(d[0:N]))


class Solution:
    # O(NLog(N)) time | O(1) space
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by a gain which company has
        # by sending a person to city A and not to city B
        costs.sort(key=lambda x: x[0] - x[1])


        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
            print(f'{costs[i][0]} + {costs[i + n][1]} = {total}')
        return total


if __name__ == '__main__':
    sol = Solution()

    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    costs2 = [[259, 770], [448, 54], [926, 667],
              [184, 139], [840, 118], [577, 469]]

    print(sol.twoCitySchedCost(costs))

    print(sol.twoCitySchedCost(costs2))
