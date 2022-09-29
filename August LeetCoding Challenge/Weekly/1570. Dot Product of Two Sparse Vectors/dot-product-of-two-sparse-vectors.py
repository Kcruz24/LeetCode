from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        # Return the dotProduct of two sparse vectors

    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for v1, v2 in zip(self.nums, vec.nums):
            product += v1 * v2

        return product
        # Your SparseVector object will be instantiated and called as such:
        # v1 = SparseVector(nums1)
        # v2 = SparseVector(nums2)
        # ans = v1.dotProduct(v2)


if __name__ == '__main__':
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]

    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    ans = v1.dotProduct(v2)
    print(ans)
