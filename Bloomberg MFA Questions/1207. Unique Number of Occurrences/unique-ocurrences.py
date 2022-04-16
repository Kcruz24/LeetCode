from typing import List
from collections import Counter


class Solution:
    # O(N) time | O(N) space
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr)
        unique_occurrences = set()

        for _, v in occurences.items():
            unique_occurrences.add(v)

        return len(unique_occurrences) == len(occurences)


if __name__ == '__main__':
    array = [1, 2, 2, 1, 1, 3]
    array2 = [1, 2]
    array3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

    sol = Solution()

    print(sol.uniqueOccurrences(array))
    print(sol.uniqueOccurrences(array2))
    print(sol.uniqueOccurrences(array3))
