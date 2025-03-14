from bisect import bisect_left
from typing import List


class Solution:
    # O(N^2) Time | O(N) Space
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)

        dp = [1] * size  # [1, 1, 1, 1, 1, 1,]

        ptr1 = 1
        ptr2 = 1
        ptr3 = 0

        while ptr3 < size:
            subsequence_length = 0

            while ptr1 > 0:
                if nums[ptr1] < nums[ptr2]:
                    subsequence_length += 1
                    ptr2 = ptr1

                ptr1 -= 1

            dp[ptr3] += subsequence_length
            ptr3 += 1
            ptr2 = ptr3
            ptr1 = ptr2 - 1

        print(dp)
        return max(dp)


class Solution2:
    # O(N^2) Time | O(N) Space
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1] * size

        for i in range(1, size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Solution3:
    # O(N^2) Time | O(N) Space
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        longest_subsequence = [nums[0]]

        for i in range(1, size):

            if nums[i] > longest_subsequence[-1]:
                longest_subsequence.append(nums[i])
            else:
                for sub in range(len(longest_subsequence)):
                    if nums[i] <= longest_subsequence[sub]:
                        longest_subsequence[sub] = nums[i]
                        break

        return len(longest_subsequence)


class Solution4:
    # O(Nlog(N))) Time | O(N) Space
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        longest_subsequence = [nums[0]]

        for i in range(1, size):

            if nums[i] > longest_subsequence[-1]:
                longest_subsequence.append(nums[i])
            else:
                idx = bisect_left(longest_subsequence, nums[i])
                longest_subsequence[idx] = nums[i]

        return len(longest_subsequence)


    def __binary_search(self, arr, target):
        start = len(arr)
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                arr[mid] = target
            elif arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1



if __name__ == '__main__':
    sol = Solution4()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(sol.lengthOfLIS(nums))

    nums = [0,1,0,3,2,3]
    print(sol.lengthOfLIS(nums))