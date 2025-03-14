'''
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

queries = [
    [1,0],
    [-3,1],
    [-4,0],
    [2,3]
]

map = {
    0: 2
    1: -1
    2: 3
    3: 4
}
res = [8, 6]
sum = 4
nums = [-2, -1, 3, 4]
output = [8, 6, 2, 4]
'''

class Solution:
    # O(N + Q) Time | O(Q) Space
    def sumEvenAfterQueries(self, nums, queries):
        running_sum = sum([num for num in nums if num % 2 == 0])
        output = []

        for query, idx in queries:
            val = nums[idx] + query

            if nums[idx] % 2 == 0:
                running_sum -= nums[idx]

            nums[idx] = val
            running_sum += nums[idx] if nums[idx] % 2 == 0 else 0

            output.append(running_sum)

        return output


if __name__ == '__main__':
    sol = Solution()

    nums = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]

    print(sol.sumEvenAfterQueries(nums, queries))