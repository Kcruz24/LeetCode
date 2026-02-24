'''


Steps:
    1. Look for the two numbers with the smallest difference
    2. Remove one of them and change the other to be equal to the result
       of the difference
    3. Keep repeating the steps until we have one number left.
'''
from typing import List


class Solution:
    # Does not work
    # O(N^3) Time | O(1) Space
    def lastStoneWeightII(self, stones: List[int]) -> List[int]:
        smallest_diff = float('inf')
        x, y = 0, 0

        while len(stones) > 1:

            for i in range(len(stones)):
                for j in range(i + 1, len(stones)):
                    diff = abs(stones[i] - stones[j])
                    if diff < smallest_diff:
                        smallest_diff = diff
                        x = i
                        y = j

            if stones[x] == stones[y]:
                if x < len(stones):
                    stones.pop(x)
                if y < len(stones):
                    stones.pop(y)
            else:
                if x < len(stones):
                    stones.pop(x)
                if y < len(stones):
                    stones[y] = smallest_diff

            smallest_diff = float('inf')

        return stones[0]


if __name__ == '__main__':
    sol = Solution()

    stones = [2, 7, 4, 1, 8, 1]
    print(sol.lastStoneWeightII(stones))

    stones = [31, 26, 33, 21, 40]
    print(sol.lastStoneWeightII(stones))
