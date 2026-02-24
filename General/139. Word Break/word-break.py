'''

Input: s = "catsandog"
       wordDict = ["cats","dog","sand","and","cat"]

Output: False

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

cats and og = False
cat sand og = False


s = "applepenapple"
wordDict = ["apple","pen"]

apple pen apple = True

'''
from typing import List
from collections import deque

# Brute Force
class Solution:
    # O(2^N) Time | O(N) Space
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, set(wordDict), 0)

    def helper(self, s, word_dict, start):
        string_length = len(s)
        if start == string_length:
            return True

        for end in range(start + 1, string_length + 1):
            if s[start:end] in word_dict and self.helper(s, word_dict, end):
                return True

        return False


# BFS
class Solution:
    # O(N^3) Time | O(N) Space
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        seen = set()
        queue = deque([0])

        while queue:
            start_node = queue.popleft()

            if start_node in seen:
                continue

            for end in range(start_node + 1, len(s) + 1):
                if s[start_node:end] in word_set:
                    queue.append(end)
                    if end == len(s):
                        return True

            seen.add(start_node)

        return False


if __name__ == '__main__':
    sol = Solution()

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s, wordDict))

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(sol.wordBreak(s, wordDict))
