from typing import List

# Brute Force


class Solution:
    # O((N + M)(log(N + M)) Time | O(N) Space
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]

        nums1.sort()

# Optimal


class Solution2:
    # O(N + M) Time | O(N) Space
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]

        ptr1 = 0
        ptr2 = 0
        ptr3 = 0

        while ptr3 < len(nums1):
            if ptr2 >= n or ptr1 < m and nums1_copy[ptr1] <= nums2[ptr2]:
                nums1[ptr3] = nums1_copy[ptr1]
                ptr1 += 1
            else:
                nums1[ptr3] = nums2[ptr2]
                ptr2 += 1

            ptr3 += 1

        return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol = Solution2()

    print(sol.merge(nums1, m, nums2, n))
