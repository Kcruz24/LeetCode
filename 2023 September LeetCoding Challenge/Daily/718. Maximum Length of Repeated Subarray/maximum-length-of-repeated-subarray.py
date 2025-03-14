from collections import defaultdict
from typing import List


'''
Input: nums1 = [1,2,3,2,1]
                |
       nums2 = [3,2,1,4,7]
                |

Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
'''


# Brute Force
class Solution:
    # O(M*N*min(M,N)) Time | O(N) Space
    def findLength(self, A, B):
        ans = 0
        Bstarts = defaultdict(list)
        for j, y in enumerate(B):
            Bstarts[y].append(j)

        for i, x in enumerate(A):
            for j in Bstarts[x]:
                k = 0
                while i + k < len(A) and j + k < len(B) and A[i + k] == B[j + k]:
                    k += 1
                ans = max(ans, k)

        return ans


# Dynamic Programming approach
class Solution:
    # O(M*N) Time | O(M*N) Space
    def findLength(self, nums1, nums2):
        a_length = len(nums1)
        b_length = len(nums2)
        memo = [[0] * (b_length + 1) for _ in range(a_length + 1)]

        for i in range(a_length - 1, -1, -1):
            for j in range(b_length - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1

        return max(max(row) for row in memo)


# Sliding Window
class Solution:
    # O(M*N) Time | O(1) Space
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        """
        [0,0,0,0,1]
        [1,0,0,0,0]
        """
        # left to right sliding
        for k in range(len(nums1)):
            s = 0
            for (x1, x2) in zip(nums1[k:], nums2):
                if x1 == x2:
                    s += 1
                else:
                    res = max(res, s)
                    s = 0
            res = max(res, s)

        # right to left sliding
        for k in range(len(nums2)):
            s = 0
            for (x1, x2) in zip(nums2[k:], nums1):
                if x1 == x2:
                    s += 1
                else:
                    res = max(res, s)
                    s = 0
            res = max(res, s)

        return res
