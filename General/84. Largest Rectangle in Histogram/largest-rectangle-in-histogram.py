from itertools import chain
from typing import List


class Solution:
    # O(N^3) Time | O(1) Space
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        size = len(heights)
        for i in range(size):
            for j in range(i, size):
                min_height = float('inf')

                for k in range(i, j + 1):
                    min_height = min(min_height, heights[k])

                max_area = max(min_height * (j - i + 1), max_area)

        return max_area


class Solution:
    # O(N^2) Time | O(1) Space
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        size = len(heights)
        for i in range(size):
            min_height = float('inf')

            for j in range(i, size):
                min_height = min(min_height, heights[j])
                max_area = max(min_height * (j - i + 1), max_area)

        return max_area


class Solution:
    # O(N) Time | O(N) Space
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        stack = []

        for idx, height in enumerate(chain([0], heights, [0])):
            while stack and stack[-1][1] > height:
                rect_right = idx
                rect_height = stack.pop()[1]
                rect_left = stack[-1][0]
                area = (rect_right - rect_left - 1) * rect_height
                max_area = max(max_area, area)

            stack.append((idx, height))

        return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]

    sol = Solution().largestRectangleArea(heights)
    print(sol)
