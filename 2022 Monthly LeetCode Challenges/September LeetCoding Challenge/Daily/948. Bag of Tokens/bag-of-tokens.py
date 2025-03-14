import heapq
from typing import List

'''


tokens = [100, 200]

power = 250
score = 1

tokens = [100, 200, 300, 400]
power = 0
score = 2


tokens = [100, 200, 300, 400, 500, 600, 700, 800]

power = 800
score = 1

'''


class Solution:
    # O(Nlog(N)) Time | O(1) Space
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        score = 0
        max_score = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1

                max_score = max(score, max_score)

            elif power < tokens[left] and score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break

        return max_score


if __name__ == '__main__':
    sol = Solution()

    tokens = [100, 200, 300, 400]
    power = 200

    print(sol.bagOfTokensScore(tokens, power))

    tokens = [26]
    power = 51

    print(sol.bagOfTokensScore(tokens, power))