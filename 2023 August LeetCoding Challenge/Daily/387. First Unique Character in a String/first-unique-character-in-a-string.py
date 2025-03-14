from collections import Counter

class Solution:
    # O(N) Time | O(1) Space
    def firstUniqChar(self, s: str) -> int:
        frequencies = Counter(s)

        for idx, char in enumerate(s):
            if frequencies[char] == 1:
                return idx

        return -1