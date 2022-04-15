from typing import List
import heapq


class Solution:
    # Does not work
    # O(N^2) time | O(1) space
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(lambda x: x[0])

        used_rooms = 0

        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if intervals[j][1] <= intervals[i][0]:
                    used_rooms += 1
                    break

        return used_rooms


class Solution2:
    # O(NLog(N)) time | O(N) space
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals is None:
            return 0

        sorted_end_times = sorted(intervals, key=lambda x: x[1])
        sorted_start_times = sorted(intervals, key=lambda x: x[0])

        minimum_rooms = 0

        start_ptr = 0
        end_ptr = 0

        while start_ptr < len(sorted_start_times):
            start_time = sorted_start_times[start_ptr][0]
            end_time = sorted_end_times[end_ptr][1]

            if start_time < end_time:
                minimum_rooms += 1
                start_ptr += 1
            else:
                start_ptr += 1
                end_ptr += 1

        return minimum_rooms


class Solution3:
    # O(NLog(N)) time | O(N) space
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)


class Solution4:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)
        meeting_rooms = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            conference = sorted_intervals[i]
            meeting_room_is_availble = False
            j = 0
            idx = 0
            while j < len(meeting_rooms) and not meeting_room_is_availble:
                meeting_room = meeting_rooms[j]
                if conference[0] >= meeting_room[1]:
                    idx = j
                    meeting_room_is_availble = True
                j += 1

            if meeting_room_is_availble:
                meeting_rooms[idx] = conference
            else:
                meeting_rooms.append(conference)

        return len(meeting_rooms)

if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]

    sol = Solution2()

    print(sol.minMeetingRooms(intervals))

    rooms = [3, 4, 1, 2, 5]

    rooms = [-1 * x for x in rooms]

    print(rooms)

    rooms.sort()
    heapq.heapify(rooms)
    print(rooms)

    heapq.heappush(rooms, 7)

    print(rooms)

    print(heapq.heappop(rooms) * -1)

    print(rooms)

    heapq.heappop(rooms)

    print(rooms)
