from typing import List

'''
boxTypes = [[1,3], -> 3
            [2,2], -> 4
            [3,1] -> 3
        ]

truckSize = 4


'''

# Brute Force


class Solution:
    # O(N^2) Time | O(1) Space
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        unit_count = 0
        remaining_truck_size = truckSize

        while remaining_truck_size > 0:
            max_unit_box_idx = self.find_max_unit_box_idx(boxTypes)

            if max_unit_box_idx == -1:
                break

            box_count = min(remaining_truck_size,
                            boxTypes[max_unit_box_idx][0])
            unit_count += box_count * boxTypes[max_unit_box_idx][1]

            remaining_truck_size -= box_count

            boxTypes[max_unit_box_idx][1] = -1

        return unit_count

    def find_max_unit_box_idx(self, boxTypes):
        max_unit_box_idx = -1
        max_units = 0

        for idx in range(len(boxTypes)):
            if boxTypes[idx][1] > max_units:
                max_units = boxTypes[idx][1]
                max_unit_box_idx = idx

        return max_unit_box_idx
