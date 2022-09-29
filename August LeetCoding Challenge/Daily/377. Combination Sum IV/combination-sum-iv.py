from math import comb
from typing import List

'''
Input: nums = [1,2,3], target = 4
Output: 7

(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(2, 1, 1)
(1, 3)
(3, 1)
(2, 2)
Total = 7



nums = [1], target = 1

(1)
Total = 1

nums = [1, 2], target 3
(1, 1, 1)
(1, 2)
(2, 1)



'''

# Top-Down dynamic programming
class Solution:
    # O(TxN) Time | O(T) Space
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.combs(nums, target)

    def combs(self, nums, remain):
        if remain == 0:
            return 1

        result = 0
        for num in nums:
            if remain - num >= 0:
                result += self.combs(nums, remain - num)

        return result


# Bottom-Up dynamic programming
class Solution2:
    # O(TxN) Time | O(T) Space
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for comb_sum in range(target + 1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum - num]

        return dp[target]




if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3]
    target = 4

    print(sol.combinationSum4(nums, target))





