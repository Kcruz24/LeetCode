from typing import List


class Solution:
    # O(N) Time | O(1) Space
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        snowBallSize = 0

        for idx, num in enumerate(nums):
            if num == 0:
                snowBallSize += 1
            elif snowBallSize > 0:
                nums[idx - snowBallSize] = nums[idx]
                nums[idx] = 0

        return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    nums2 = [0, 1, 0, -1, -3, -2, 3, 12]

    sol = Solution()

    print(sol.moveZeroes(nums))
    print(sol.moveZeroes(nums2))
