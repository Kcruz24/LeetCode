
'''
Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is

["a","b","aa","bb","ab","ba","aab", "abb","bab","bba","aba","aabb","abba",
"bbab","baba","aabba","abbab","bbaba", "aabbab","abbaba","aabbaba"]
'''


class Solution:
    # O(N^2) Time | O(N) Space
    def countDistinct(self, s: str) -> int:
        substrings = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substrings.append(s[i:j])

        return len(set(substrings))
