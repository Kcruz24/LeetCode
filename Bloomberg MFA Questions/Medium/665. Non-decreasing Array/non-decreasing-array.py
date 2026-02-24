
'''

- Look for the number that is unsorted
- Change that number to be 1 less than the number in front
- Check if the array is sorted, if it is, return True, otherwise return False

'''
from typing import List

# DOES NOT WORK - 319/335 passed


class Solution:
    # O(Nlog(N)) Time | O(1) Space
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i] = nums[i + 1] - 1
                break

        return nums == sorted(nums)

# DOES NOT WORK - 320/335 passed


class Solution:
    # O(N) Time | O(1) Space
    def checkPossibility(self, nums: List[int]) -> bool:

        violations = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                violations += 1

            if violations > 1:
                return False

        return True


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


if __name__ == '__main__':
    sol = Solution()

    nums = [4, 2, 3]
    print(sol.checkPossibility(nums))

    nums = [4, 2, 1]
    print(sol.checkPossibility(nums))

    nums = [1, 2, 3, 4, 8, 6, 7, 8, 9]
    print(sol.checkPossibility(nums))

    nums = [5, 7, 1, 8]
    print(sol.checkPossibility(nums))
