'''
intervals = [
    [1,3],
    [2,6],
    [8,10],
    [15,18]
    ]


[1, 6], [8, 10], [15, 18]

[[1,6],[8,10],[15,18]]
'''


from typing import List


class Solution:
    # O(NLog(N)) Time | O(N) Space
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = [intervals[0]]

        for interval in intervals[1:]:
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(interval[1], merged[-1][1])
            else:
                merged.append(interval)

        return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    sol = Solution().merge(intervals)
    print(sol)

    intervals = [[1, 4], [4, 5]]
    sol = Solution().merge(intervals)
    print(sol)
