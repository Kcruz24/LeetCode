from typing import List


# Brute Force
class Solution:
    # O(N^3) Time | O(1) Space
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] > nums[k] and \
                       nums[i] + nums[k] > nums[j] and \
                       nums[j] + nums[k] > nums[i]:
                        count += 1

        return count

# Binary Search


class Solution2:
    # O(n^2 * log(n)) Time | O(log(n)) Space
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()

        for i in range(len(nums) - 2):
            k = i + 2
            if nums[i] != 0:
                for j in range(i + 1, len(nums) - 1):
                    k = self.binary_search(
                        nums, k, len(nums) - 1, nums[i] + nums[j])
                    count += k - j - 1

        return count

    def binary_search(self, arr, start, end, target):
        while end >= start and end < len(arr):
            mid = (start + end) // 2
            if arr[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1

        return start


# Linear Scan
class Solution3:
    # O(N^2) Time | O(log(N)) Space
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()

        for i in range(len(nums) - 2):
            k = i + 2
            if nums[i] != 0:
                for j in range(i + 1, len(nums) - 1):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    count += k - j - 1

        return count


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()

    nums = [2, 2, 3, 4]
    print(sol.triangleNumber(nums))

    nums = [2, 2, 3, 4]
    print(sol2.triangleNumber(nums))
