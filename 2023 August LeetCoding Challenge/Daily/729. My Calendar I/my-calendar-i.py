
'''

- Sort the start times and end times

[1, 3]

'''


import bisect


class MyCalendar:

    def __init__(self):
        self.calendar = []

    # O(N^2) Time | O(N) Space
    def book(self, start: int, end: int) -> bool:
        for curr_start, curr_end in self.calendar:
            if curr_start < end and start < curr_end:
                return False

        self.calendar.append((start, end))
        return True


# https://leetcode.com/problems/my-calendar-i/discuss/2373132/Must-read-solution-%2B-Intuition-or-With-Image-Explanation-or-Binary-Search
class MyCalendar2:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        start_index = bisect.bisect_right(self.events, start)

        # start point must have even index
        if start_index % 2 != 0:
            return False

        end_index = bisect.bisect_left(self.events, end)

        # Both start and end must have same index before insertion
        if end_index != start_index:
            return False

        bisect.insort_right(self.events, start)
        bisect.insort_left(self.events, end)
        return True
