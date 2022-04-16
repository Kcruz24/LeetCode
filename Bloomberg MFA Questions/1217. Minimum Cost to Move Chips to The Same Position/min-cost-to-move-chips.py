from typing import List


class Solution:
    # O(N) time | O(1) space
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = 0
        odd_count = 0

        for coin in position:
            if coin % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return min(even_count, odd_count)
