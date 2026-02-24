from math import sqrt
from typing import List

'''
- are of my rectangular web page == given target area
- length >= width
- difference between width and length should be small as possible

'''


class Solution:
    # O(A) Time | O(1) Space
    def constructRectangle(self, area: int) -> List[int]:
        width = int(sqrt(area))

        while area % width != 0:
            width -= 1

        length = area // width
        web_page = [length, width]

        return web_page


if __name__ == '__main__':
    sol = Solution()

    print(sol.constructRectangle(122122))
