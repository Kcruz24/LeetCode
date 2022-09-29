from typing import List


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        output = []

        for num, query in zip(nums, removeQueries):
            nums[query] = 0
            
            output.append(sum(nums))

        return output


if __name__ == '__main__':
    sol = Solution()

    nums = [1,2,5,6,1]
    removeQueries = [0,3,2,4,1]

    print(sol.maximumSegmentSum(nums, removeQueries))