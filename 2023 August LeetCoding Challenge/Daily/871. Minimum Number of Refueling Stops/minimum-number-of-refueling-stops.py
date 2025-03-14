from typing import List
import heapq


class Solution:
    # O(N^2) Time | O(N) Space
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if not stations:
            return 0

        dp = [startFuel] + [0] * len(stations)

        for i, station in enumerate(stations):
            location, capacity = station
            for stop in range(i, -1, -1):
                if dp[stop] >= location:
                    dp[stop + 1] = max(dp[stop + 1], dp[stop] + capacity)

        for i, d in enumerate(dp):
            if d >= target:
                return i

        return -1


class Solution:
    # O(Nlog(N)) Time | O(N) Space
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append((target, float('inf')))

        ans = 0
        prev = 0

        for location, capacity in stations:
            startFuel -= location - prev
            while pq and startFuel < 0: # Must refuel in past
                startFuel += heapq.heappop(pq) * -1
                ans += 1

            if startFuel < 0:
                return -1

            heapq.heappush(pq, capacity * -1)
            prev = location

        return ans


if __name__ == '__main__':
    sol = Solution()

    target = 100
    startFuel = 10
    stations = [[10,60],[20,30],[30,30],[60,40]]

    print(sol.minRefuelStops(target, startFuel, stations))