from collections import defaultdict

# O(1) time | O(P + S^2) space - where "P" is the number of people and "S" is
# the number of stations.
class UndergroundSystem:

    def __init__(self):
        self.people_info = {}
        self.travel_times = defaultdict(lambda: [0, 0])

    # O(1) time | O(N) space
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people_info[id] = (stationName, t)

    # O(1) time | O(N) space
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.people_info.pop(id)

        self.travel_times[(start_station, stationName)][0] += (t - start_time)
        self.travel_times[(start_station, stationName)][1] += 1

    # O(1) time | O(N) space
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, travel_count = self.travel_times[(startStation, endStation)]

        return total_time / travel_count



if __name__ == '__main__':
    system = UndergroundSystem()

    system.checkIn(45, 'Leyton', 3)
    system.checkIn(32, 'Paradise', 8)
    system.checkIn(27, 'Leyton', 10)

    system.checkOut(45, 'Waterloo', 15)
    system.checkOut(27, 'Waterloo', 20)
    system.checkOut(32, 'Cambridge', 22)

    print(system.getAverageTime('Paradise', 'Cambridge'))
    print(system.getAverageTime('Leyton', 'Waterloo'))

    system.checkIn(10, 'Leyton', 24)

    print(system.getAverageTime('Leyton', 'Waterloo'))

    system.checkOut(10, 'Waterloo', 38)

    print(system.getAverageTime('Leyton', 'Waterloo'))
