from typing import List

'''

nums = [1,2,3,3,4,5]

1, 2, 3
        3
3, 4, 5


'''

# DOES NOT WORK
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = 1
        next_idx = 0
        for idx in range(len(nums) - 1):
            if nums[idx] < nums[idx + 1]:
                count += 1

            if count == 3:
                next_idx = idx + 1
                break

        print(nums[next_idx:])
        for idx in range(len(nums[next_idx:]) - 1):
            if nums[idx] < nums[idx + 1]:
                count += 1

        return count >= 6


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3, 3, 4, 5]
    print(sol.isPossible(nums))

    nums = [1, 2, 3, 4, 4, 5]
    print(sol.isPossible(nums))
