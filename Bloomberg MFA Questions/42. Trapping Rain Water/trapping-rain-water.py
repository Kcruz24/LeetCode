from typing import List


class Solution:
    # O(N) Time | O(1) Space
    def trap(self, height: List[int]) -> int:
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size

        left_max[0] = height[0]
        for idx in range(1, size):
            left_max[idx] = max(height[idx], left_max[idx - 1])

        right_max[-1] = height[-1]
        for idx in range(size - 2, -1, -1):
            right_max[idx] = max(height[idx], right_max[idx + 1])

        water_trapped = 0
        for idx, num in enumerate(height):
            water_trapped += min(right_max[idx], left_max[idx]) - num

        return water_trapped


class Solution:
    # O(N) Time | O(1) Space
    def trap(self, height):
        size = len(height)

        left = 0
        right = size - 1

        left_max = 0
        right_max = 0

        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]

                right -= 1

        return ans



if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    sol = Solution().trap(height)
    print(sol)