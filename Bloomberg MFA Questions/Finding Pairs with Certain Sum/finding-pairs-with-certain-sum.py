from typing import List
from collections import defaultdict, Counter

# Brute Force


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

    # O(1) time | O(1) space
    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    # O(N^2) time | O(N) space
    def count(self, tot: int) -> int:
        pairs = []
        nums1_length = len(self.nums1)
        nums2_length = len(self.nums2)

        for i in range(nums1_length):
            for j in range(nums2_length):
                num1 = self.nums1[i]
                num2 = self.nums2[j]

                if num1 + num2 == tot:
                    pairs.append((i, j))

        return len(pairs)


# Optimal - Time limit exceeded
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

    # O(1) time | O(1) space
    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    # Avg: O(N) time | O(N) space
    # Worst: O(N^2) time | O(N) space
    def count(self, tot: int) -> int:
        pairs = []

        hashMap = defaultdict(list)

        for idx, num in enumerate(self.nums2):
            hashMap[num].append(idx)

        for num in self.nums1:
            potential_match = tot - num

            if potential_match not in hashMap:
                continue

            for pair in hashMap[potential_match]:
                pairs.append((num, pair))

        print(pairs)
        return len(pairs)


# Optimal solution from leetcode discussions
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/discuss/1211065/JavaPython-Two-sum-problem-using-HashMap-Clean-and-Concise
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    # O(1) time | O(1) space
    def add(self, index: int, val: int) -> None:
        self.freq[nums2[index]] -= 1
        self.nums2[index] += val
        self.freq[nums2[index]] += 1

    # O(N) time | O(N) space
    def count(self, tot: int) -> int:
        pairsSum = 0

        for num in self.nums1:
            potential_match = tot - num
            pairsSum += self.freq[potential_match]

        return pairsSum


if __name__ == '__main__':
    nums1 = [1, 1, 2, 2, 2, 3]
    nums2 = [1, 4, 5, 2, 5, 4]

    num_map = Counter(nums2)

    print(num_map)
    for k, v in num_map.items():
        print(k, ':', v)

    sumPairs = FindSumPairs(nums1, nums2)

    # print(sumPairs.count(1))

    target = 1
