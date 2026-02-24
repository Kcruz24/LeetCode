from math import sqrt


class Solution:
    # O(log(N)) Time | O(1) Space
    def constructRectangle(self, area):
        x = int(sqrt(area))

        while area % x != 0:
            x -= 1

        return [area / 2, x]
