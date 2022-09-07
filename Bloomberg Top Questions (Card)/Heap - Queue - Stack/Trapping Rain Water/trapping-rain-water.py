from typing import List

# Dynamic Programming
class Solution:
    # O(N) Time | O(N) Space
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        size = len(height)
        left_max = [0] * size
        right_max = [0] * size

        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        ans = 0
        for i in range(size):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


# Using Stack - Does not work
class Solution:
    # O(N) Time | O(N) Space
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        curr = 0

        while curr < len(height):
            while stack and height[curr] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()

                if not stack:
                    break

                distance = curr - stack[-1] - 1
                bounded_height = min(
                    height[curr], height[stack[-1]]) - height[top]

                ans += distance * bounded_height

            curr += 1
            stack.append(curr)

        return ans


# Two Pointers
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
    sol = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(sol.trap(height))

    height = [4, 2, 0, 3, 2, 5]
    print(sol.trap(height))
