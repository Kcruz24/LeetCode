from typing import List


# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == val:
                nums.pop(i)

            i += 1

        return len(nums)


if __name__ == '__main__':

    nums = [3, 2, 2, 3]
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]

    val = 3
    val2 = 2

    sol = Solution2()

    print(sol.removeElement(nums, val))
    print(sol.removeElement(nums2, val2))
