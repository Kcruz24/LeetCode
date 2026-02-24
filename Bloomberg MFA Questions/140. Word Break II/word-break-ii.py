from typing import List

'''
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

"cat sand dog"
"cats and dog"
"catsanddog"
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(res, sol, s, wordDict):
            if len(s) == 0:
                res.append(" ".join(sol))
                return

            for w in wordDict:
                if s.startswith(w):
                    sol.append(w)
                    backtrack(res, sol, s[len(w):], wordDict)
                    sol.pop()

        res = []
        backtrack(res, [], s, wordDict)
        return res


# From: https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
class Solution2:
    def wordBreak(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        '''
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue

            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)

        memo[s] = res
        return res


if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cats", "and", "sand", "dog", "cat"]

    sol = Solution()

    print(sol.wordBreak(s, wordDict))
