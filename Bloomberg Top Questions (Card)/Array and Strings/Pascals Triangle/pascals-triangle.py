from typing import List


class Solution:
    # O(N^2) Time | O(1) Space
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            sub_list = [None for _ in range(row + 1)]
            sub_list[0], sub_list[-1] = 1, 1

            for j in range(1, len(sub_list) - 1):
                sub_list[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(sub_list)

        return triangle
