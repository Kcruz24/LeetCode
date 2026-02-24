
from typing import List


class Solution:
    # O(N) Time | O(1) Space
    def checkPossibility(self, nums: List[int]) -> bool:
        violations = 0
        for i in range(1, len(nums)):

            if nums[i - 1] > nums[i]:
                if violations == 1:
                    return False

                violations += 1

                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]

                elif nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]

        return True


class Solution:
    # O(N^2) Time | O(N) Space
    def checkPossibility(self, nums):
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        nums_copy = nums.copy()
        for i in range(len(nums)):
            original_num = nums[i]
            nums_copy[i] = nums_copy[i-1] if i > 0 else float('-inf')

            if monotone_increasing(nums_copy):
                return True

            nums_copy[i] = original_num

        return False


if __name__ == '__main__':
    sol = Solution()

    nums = [4, 2, 3]
    print(sol.checkPossibility(nums))
