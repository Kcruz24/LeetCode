'''

Input: s = "abcabcbb"
            ||

        "asdfasdfjklasdf"

set = [a, b, c]
Output: 3
'''


class Solution:
    # Brute Force
    # O(N^2) Time | O(N) Space
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 1

        for i in range(len(s) - 1):
            char = s[i]
            running_counter = 1
            seen = set()

            for j in range(i + 1, len(s)):
                char2 = s[j]

                if char == char2 or char2 in seen:
                    break
                seen.add(char2)

                running_counter += 1
                longest = max(longest, running_counter)

        return longest


class Solution:
    # Optimal - Sliding Window
    # O(N) Time | O(N) Space
    def lengthOfLongestSubstring(self, s: str) -> int:
        dups = set()

        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in dups:
                dups.remove(s[left])
                left += 1

            dups.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
