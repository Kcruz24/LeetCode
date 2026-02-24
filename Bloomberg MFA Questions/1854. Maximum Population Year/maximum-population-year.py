from typing import List


class Solution:
    # O(NLog(N)) Time | O(N) Space
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))

        dates.sort()

        population = max_population = max_year = 0
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = year


        return max_year


class Solution:
    # O(Nlog(N)) Time | O(N) Space
    def maximumPopulation(self, logs):
        births = sorted([birth for birth, _ in logs])
        deaths = sorted([death for _, death, in logs])

        b_ptr = 0
        d_ptr = 0

        population = 0
        max_population = 0
        max_year = 0
        while b_ptr < len(logs):
            if births[b_ptr] < deaths[d_ptr]:
                population += 1

                if population > max_population:
                    max_population = population
                    max_year = births[b_ptr]

                b_ptr += 1
            else:
                population -= 1
                d_ptr += 1

        return max_year


class Solution:
    # O(N) Time | O(1) Space
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # the timespan 1950-2050 covers 101 years
        delta = [0] * 101

        # to make explicit the conversion from the year (1950 + i) to the ith index
        conversionDiff = 1950

        for l in logs:
            # the log's first entry, birth, increases the population by 1
            delta[l[0] - conversionDiff] += 1

            # the log's second entry, death, decreases the population by 1
            delta[l[1] - conversionDiff] -= 1

        runningSum = 0
        maxPop = 0
        year = 1950

        # find the year with the greatest population
        for i, d in enumerate(delta):
            runningSum += d

            # since we want the first year this population was reached, only update if strictly greater than the previous maximum population
            if runningSum > maxPop:
                maxPop = runningSum
                year = conversionDiff + i

        return year

if __name__ == '__main__':
    sol = Solution()

    logs = [[1950, 1961], [1965, 1971], [1966, 1981], [1967, 1983]]

    print(sol.maximumPopulation(logs))
