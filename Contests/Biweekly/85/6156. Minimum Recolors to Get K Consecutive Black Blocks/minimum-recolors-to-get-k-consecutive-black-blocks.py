from collections import Counter

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = Counter(blocks)

        blocks.sort()

        if counter['B'] >= k:
            return 0

        min_operations = counter['B']
        for block in blocks:
            if block == 'W':
                min_operations += 1

            if min_operations == k:
                return min_operations

        return -1