from typing import List


class Solution:
    # O(NLog(N)) Time | O(1) Space
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(slots1) and ptr2 < len(slots2):
            start1, end1 = slots1[ptr1]
            start2, end2 = slots2[ptr2]

            common = [max(start1, start2), min(end1, end2)]
            if common[1] - common[0] >= duration:
                return [common[0], common[0] + duration]

            if end1 < end2:
                ptr1 += 1
            else:
                ptr2 += 1

        return []


if __name__ == '__main__':
    sol = Solution()

    slots1 = [[10, 50], [60, 120], [140, 210]]
    slots2 = [[0, 15], [60, 70]]
    duration = 8

    print(sol.minAvailableDuration(slots1, slots2, duration))
