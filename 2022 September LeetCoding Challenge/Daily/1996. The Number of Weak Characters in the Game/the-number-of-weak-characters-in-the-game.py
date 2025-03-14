'''

Input: properties = [
                   0: [5,5],
                   1: [6,3],
                   2: [3,6]]

[1, 5],
[4, 3],
[10, 4],

Output: 0


[[1,1],
 [1,2]
 [2,1],
 [2,2],

[[1,1],
 [1,2]
 [2,1],
 [2,2],
'''

from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_defense = properties[0][1]

        weak = 0
        for _, defense in properties:
            if defense < max_defense:
                weak += 1
            else:
                max_defense = defense

        return weak


if __name__ == '__main__':
    properties = [[1, 1],
                  [1, 2],
                  [2, 1],
                  [2, 2]]

    sol = Solution()
    print(sol.numberOfWeakCharacters(properties))
