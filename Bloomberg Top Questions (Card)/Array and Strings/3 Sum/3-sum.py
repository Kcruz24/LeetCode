from typing import List


class Solution:
    # O(N^2) time | O(N) space
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target_sum = 0
        triplets = []

        nums.sort()

        for idx in range(len(nums)):
            if nums[idx] > 0:
                break

            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue
            
            self.twoSumII(nums, target_sum, idx, triplets)

        return triplets

    def twoSumII(self, numbers: List[int], target: int, i: int, triplets: List[int]) -> List[int]:
        left_ptr = i + 1
        right_ptr = len(numbers) - 1

        while left_ptr < right_ptr:
            left_num = numbers[left_ptr]
            right_num = numbers[right_ptr]
            curr_num = numbers[i]

            sum = curr_num + left_num + right_num
            sum_list = [curr_num, left_num, right_num]

            if sum < target:
                left_ptr += 1
            elif sum > target:
                right_ptr -= 1
            else:
                triplets.append(sum_list)
                left_ptr += 1
                right_ptr -= 1

                while left_ptr < right_ptr and numbers[left_ptr] == numbers[left_ptr - 1]:
                    left_ptr += 1


if __name__ == '__main__':
    values = [-1, 0, 1, 2, -1, -4]
    values2 = [0, 0, 0]
    values3 = [0, 0, 0, 0]
    values4 = [-2, 0, 0, 2, 2]

    sol = Solution()

    print(sol.threeSum(values))
    print(sol.threeSum(values2))
    print(sol.threeSum(values3))
    print(sol.threeSum(values4))
