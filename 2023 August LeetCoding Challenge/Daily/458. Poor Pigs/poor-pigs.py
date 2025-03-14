from math import ceil, log

'''

buckets = 4
minutesToDie = 15
minutesToTest = 15

'''

class Solution:
    # O(1) Time | O(1) Space
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        return ceil(log(buckets) / log(states))