from typing import List

'''
Input: strs = ["flower","flow","flight"]
Output: "fl"

'''

# Horizontal Scanning Technique


class Solution:
    # O(S) Time | O(1) Space - Where 'S' is the sum of all characters in all strings
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

        return prefix


if __name__ == '__main__':

    sol = Solution()
    strs = ["flower", "flow", "flight"]

    print(sol.longestCommonPrefix(strs))
