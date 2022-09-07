from typing import List


class Solution:
    # O(Nlog(N)) Time | O(N) Space
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = []
        end_time = []

        for start, end in intervals:
            start_time.append(start)
            end_time.append(end)

        start_time.sort()
        end_time.sort()

        start_ptr = 0
        end_ptr = 0
        used_rooms = 0

        while start_ptr < len(intervals):
            if start_time[start_ptr] < end_time[end_ptr]:
                used_rooms += 1
            else:
                end_ptr += 1

            start_ptr += 1
        return used_rooms


if __name__ == '__main__':
    sol = Solution()

    intervals = [[0, 30], [5, 10], [15, 20]]

    print(sol.minMeetingRooms(intervals))

    intervals = [[7, 10], [2, 4]]
    print(sol.minMeetingRooms(intervals))
