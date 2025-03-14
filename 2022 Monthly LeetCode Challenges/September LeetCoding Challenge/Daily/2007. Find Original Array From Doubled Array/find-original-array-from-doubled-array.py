from collections import Counter
from typing import List


class Solution:
    # O(Nlog(N)) Time | O(N) Space
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        changed.sort()

        freq = Counter(changed)

        original = []
        for num in changed:
            if freq[num] > 0:
                freq[num] -= 1

                if num * 2 in freq and freq[num * 2] > 0:
                    freq[num * 2] -= 1
                    original.append(num)
                else:
                    return []

        return original
