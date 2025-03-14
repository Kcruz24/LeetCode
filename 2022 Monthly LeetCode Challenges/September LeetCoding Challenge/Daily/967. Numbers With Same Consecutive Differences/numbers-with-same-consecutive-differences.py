from collections import deque
from typing import List


# DFS
class Solution:
    # O(2^N) Time | O(2^N) Space
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        if n == 1:
            return [num for num in range(10)]

        def dfs(n, num):
            if n == 0:
                return ans.append(num)

            tail_digit = num % 10
            next_digits = set([tail_digit + k, tail_digit - k])

            for digit in next_digits:
                if 0 <= digit < 10:
                    new_num = num * 10 + digit
                    dfs(n - 1, new_num)


        ans = []
        for num in range(1, 10):
            dfs(n - 1, num)

        return list(ans)


# BFS
class Solution:
    # O(2^N) Time | O(2^N) Space
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [num for num in range(10)]

        queue = deque([num for num in range(1, 10)])

        def bfs():
            size = len(queue)
            for _ in range(size):
                num = queue.popleft()
                
                tail_digit = num % 10
                next_digits = set([tail_digit + k, tail_digit - k])

                for digit in next_digits:
                    if 0 <= digit < 10:
                        new_num = num * 10 + digit
                        queue.append(new_num)

        for level in range(n - 1):
            bfs()

        return queue


if __name__ == '__main__':
    n = 3
    k = 7

    sol = Solution().numsSameConsecDiff(n, k)
    print(sol)
