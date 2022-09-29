class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        occurrence = '01'
        seconds = 0

        while occurrence in s:
            s = s.replace(occurrence, '10')
            seconds += 1

        return seconds

