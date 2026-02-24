from typing import List


class Solution:
    # O(N*2^N) Time | O(N) Space
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.power_set(nums, 0, [], [])

    def power_set(self, nums, start, arr, all_sets):
        all_sets.append(arr.copy())

        for i in range(start, len(nums)):
            arr.append(nums[i])
            self.power_set(nums, i + 1, arr, all_sets)
            arr.pop()

        return all_sets


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3]
    print(sol.subsets(nums))
