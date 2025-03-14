import heapq
from typing import List

'''
Input: n = 6,
       speed = [2,10,3,1,5,8]
  efficiency = [5,4,3,9,7,2]
       k = 2

Output: 60
Explanation:
We have the maximum performance of the team by selecting engineer 2
(with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7).
That is, performance = (10 + 5) * min(4, 7) = 60.
'''


class Solution:
    # O(Nlog(N)) Time | O(N) Space
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = zip(efficiency, speed)
        candidates = sorted(candidates, key=lambda x: x[0], reverse=True)

        speed_heap = []
        speed_sum = 0
        performance = 0

        for curr_efficiency, curr_speed in candidates:
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap)

            heapq.heappush(speed_heap, curr_speed)

            speed_sum += curr_speed
            performance = max(performance, speed_sum * curr_efficiency)

        modulo = 10**9 + 7
        return performance % modulo


if __name__ == '__main__':
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 2

    sol = Solution().maxPerformance(n, speed, efficiency, k)
    print(sol)
