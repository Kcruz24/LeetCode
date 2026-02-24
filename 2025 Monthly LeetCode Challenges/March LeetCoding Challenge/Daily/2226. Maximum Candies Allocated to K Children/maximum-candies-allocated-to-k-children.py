from typing import List

class Solution:
    # O(Nlog(M)) Time | O(1) Space
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candies_in_pile = max(candies)

        left = 0
        right = max_candies_in_pile

        while left < right:
            middle = (left + right + 1) // 2

            if self.canAllocateCandies(candies, k, middle):
                left = middle
            else:
                right = middle - 1

        return left

    def canAllocateCandies(self, candies: List[int], k: int, num_of_candies: int) -> bool:
        max_num_of_children = 0

        for pile in candies:
            max_num_of_children += pile // num_of_candies

        return max_num_of_children >= k


if __name__ == "__main__":
    sol = Solution()

    candies = [2, 3, 6, 4, 5, 3]
    k = 5

    print(sol.maximumCandies(candies, k))