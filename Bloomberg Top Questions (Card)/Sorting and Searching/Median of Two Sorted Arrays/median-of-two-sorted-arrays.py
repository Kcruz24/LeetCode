from typing import List
import heapq

'''

'''

class Solution:
    # O(log(M + N)) Time | O(N) Space
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        half = total_length // 2

        median = 0
        if total_length % 2 == 1:
            median = self.kth_smallest(nums1, nums2, half)

        else:
            first_half_val = self.kth_smallest(nums1, nums2, half)
            second_half_val = self.kth_smallest(nums1, nums2, half - 1)

            median = (first_half_val + second_half_val) / 2

        return median

    def kth_smallest(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        idx_one = len(nums1) // 2
        idx_two = len(nums2) // 2
        elem_one = nums1[idx_one]
        elem_two = nums2[idx_two]

        if k > idx_one + idx_two:

            if elem_one > elem_two:
                return self.kth_smallest(nums1, nums2[idx_two + 1:], k - idx_two - 1)
            else:
                return self.kth_smallest(nums1[idx_one + 1:], nums2, k - idx_one - 1)

        else:

            if elem_one > elem_two:
                return self.kth_smallest(nums1[:idx_one], nums2, k)
            else:
                return self.kth_smallest(nums1, nums2[:idx_two], k)


if __name__ == '__main__':
    sol = Solution()

    nums1 = [1, 2]
    nums2 = [3, 4]

    print(sol.findMedianSortedArrays(nums1, nums2))
