from typing import List

'''

Input: nums = [1,3,8,48,10]
               0 1 2  3  4
Output: 3

'''


class Solution:
    # O(N^3) Time | O(1) Space
    def longestNiceSubarray(self, nums: List[int]) -> int:

        def check(left, right):
            for i in range(left, right):
                for j in range(i + 1, right + 1):
                    if nums[i] & nums[j] != 0:
                        return False
            return True

        n = len(nums)
        left, right = 0, 0

        res = 0
        while right < n:
            if check(left, right):
                running_subarray_size = right - left + 1
                res = max(running_subarray_size, res)
                right += 1
            else:
                left += 1

        return res


if __name__ == "__main__":
    nums = [1, 3, 8, 48, 10]

    sol = Solution().longestNiceSubarray(nums)
    print(sol)

    nums = [3,1,5,11,13]
    sol = Solution().longestNiceSubarray(nums)
    print(sol)
