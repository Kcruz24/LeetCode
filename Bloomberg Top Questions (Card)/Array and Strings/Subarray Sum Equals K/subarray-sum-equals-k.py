from collections import defaultdict
from typing import List


# Brute Force (Time Limit Exceeded)
class Solution:
    # O(N^3) Time | O(1) Space
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                sum = 0

                for i in range(start, end):
                    sum += nums[i]

                if sum == k:
                    count += 1

        return count


# More optimal, but still slow (Time Limit Exceeded)
class Solution2:
    # O(N^2) Time | O(1) Space
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            sum = 0
            for end in range(start, len(nums)):
                sum += nums[end]

                if sum == k:
                    count += 1

        return count

# Optimal (Accepted)


class Solution3:
    # O(N) Time | O(N) Space
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        map = defaultdict(int)

        map[0] = 1

        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in map:
                count += map[sum - k]

            map[sum] = map[sum] + 1

        return count


if __name__ == '__main__':

    nums = [1, 2, 3]
    k = 3

    sol = Solution3()

    print(sol.subarraySum(nums, k))
