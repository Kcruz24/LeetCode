from collections import Counter


class Solution:
    # O(N) time | O(1) space
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
