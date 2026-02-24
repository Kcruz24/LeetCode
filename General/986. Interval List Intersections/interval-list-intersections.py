from typing import List


'''
firstList = [[0,2],[5,10],[13,23],[24,25]]
                             |
secondList =[[1,5],[8,12],[15,24],[25,26]]
                      |

[1, 2], [5, 5], [8, 10], [13, 12]
'''


class Solution:
    # O(N) Time | O(N) Space
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []

        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(firstList) and ptr2 < len(secondList):
            start1, end1 = firstList[ptr1]
            start2, end2 = secondList[ptr2]

            left_intersect = max(start1, start2)
            right_intersect = min(end1, end2)

            if left_intersect <= right_intersect:
                output.append([left_intersect, right_intersect])

            if end1 < end2:
                ptr1 += 1
            else:
                ptr2 += 1

        return output


if __name__ == '__main__':
    sol = Solution()

    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(sol.intervalIntersection(firstList, secondList))

    output = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    print(output)
