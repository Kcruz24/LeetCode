from typing import List

'''

Start with the length as my initial number of trees
traverse from the last node in the array
beginning from the node behind the current
i'll traverse every other node verifying if its product is equal to the
current node value.

'''
class Solution:
    # O(N^2) Time | O(N) Space
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = pow(10, 9) + 7
        size = len(arr)
        arr.sort()
        dp = [1] * size

        index = {num: idx for idx, num in enumerate(arr)}

        for idx, num in enumerate(arr):
            for j in range(idx):
                if num % arr[j] == 0: # arr[j] is left child
                    right_child = num // arr[j]
                    if right_child in index:
                        right_child_idx = index[right_child]
                        dp[idx] += dp[j] * dp[right_child_idx]
                        dp[idx] %= mod


        return sum(dp) % mod


if __name__ == '__main__':
    sol = Solution()

    arr = [2, 4, 5, 10]
    sol.numFactoredBinaryTrees(arr)
    # print(sol.numFactoredBinaryTrees(arr))