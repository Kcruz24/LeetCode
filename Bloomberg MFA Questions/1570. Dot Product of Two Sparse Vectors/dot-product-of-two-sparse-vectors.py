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


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nums[i] = n

        # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        product = 0
        for key, val in self.nums.items():
            if key in vec.nums:
                product += val * vec.nums[key]
        return product
