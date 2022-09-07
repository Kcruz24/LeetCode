from typing import List
import heapq
from collections import deque

# TLE


class Solution:
    # O(NK) Time | O(N - K + 1) Space
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        size = len(nums)
        window = []
        end_ptr = k
        for i in range((size - k) + 1):
            subwindow = nums[i:end_ptr]
            #print(subwindow)
            max_subwindow = max(subwindow)
            window.append(max_subwindow)

            end_ptr += 1

        return window


# TLE
class Solution:
    # O(Nlog(k)) Time | O(N - K + 1) Space
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        size = len(nums)
        window = []
        end_ptr = k
        start_ptr = 0

        while end_ptr <= size:
            pq = []
            for i in range(start_ptr, end_ptr):
                heapq.heappush(pq, -nums[i])

            max_subwindow = -heapq.heappop(pq)
            window.append(max_subwindow)

            start_ptr += 1
            end_ptr += 1

        return window


class Solution:
    def maxSlidingWindow(self, nums, k):
        size = len(nums)

        if size * k == 0:
            return []

        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if queue and queue[0] == i - k:
                queue.popleft()

            # remove from queue indexes of all elements which are smaller than
            # current element nums[i]
            # last_queue_elem_idx = queue[-1]
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

        queue = deque()
        max_idx = 0

        for i in range(k):
            clean_deque(i)
            queue.append(i)

            # Compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i

        output = [nums[max_idx]]

        for i in range(k, size):
            clean_deque(i)
            queue.append(i)

            first_queue_elem_idx = queue[0]
            max_num = nums[first_queue_elem_idx]

            output.append(max_num)

        return output


class Solution:
    # O(N) Time | O(N) Space
    def maxSlidingWindow(self, nums, k):
        size = len(nums)
        if size * k == 0:
            return []

        if k == 1:
            return nums

        queue = deque()
        max_idx = 0

        for i in range(k):
            self.clean_deque(nums, queue, i, k)
            queue.append(i)

            # Compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i

        output = [nums[max_idx]]

        for i in range(k, size):
            self.clean_deque(nums, queue, i, k)
            queue.append(i)

            first_queue_elem_idx = queue[0]
            max_num = nums[first_queue_elem_idx]

            output.append(max_num)

        return output

    def clean_deque(self, nums, queue, i, k):
        if queue and queue[0] == i - k:
            queue.popleft()

        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(sol.maxSlidingWindow(nums, k))
