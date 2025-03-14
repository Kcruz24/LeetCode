from typing import List
from collections import Counter
import heapq

class Solution:
    # O(N) Time | O(N) Space
    def minSetSize(self, arr: List[int]) -> int:
        frequencies = Counter(arr)
        pq = []

        for _, value in frequencies.items():
            heapq.heappush(pq, value * -1)

        half = len(arr) // 2

        set_size = 0
        set_value_total = 0
        while set_value_total < half:
            set_value_total += heapq.heappop(pq) * -1
            set_size += 1

        return set_size