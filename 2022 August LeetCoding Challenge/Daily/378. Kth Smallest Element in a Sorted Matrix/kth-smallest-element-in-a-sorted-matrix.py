from typing import List
import heapq


class Solution:
    # O(M*N + log(K)) Time | O(N) space
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k == 0:
            return matrix[0][0]

        pq = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heapq.heappush(pq, matrix[row][col])

        element = 0
        while k:
            element = heapq.heappop(pq)
            k -= 1

        return element


if __name__ == '__main__':
    sol = Solution()

    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8

    print(sol.kthSmallest(matrix, k))
