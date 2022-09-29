from typing import List


class Solution:
    # O(N^2) Time | O(N) Space
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            sub = 0
            sub_sum = 0
            for num in nums:
                if num + sub_sum <= q:
                    sub_sum += num
                    sub += 1
            ans.append(sub)

        return ans
