from typing import List
import heapq


class Solution3:
    # O(Nlog(N)) Time | O(N) Space
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Iterate over all buildings, for each building i,
        # add (position, i) to edges.
        edges = []
        for i, build in enumerate(buildings):
            edges.append([build[0], i])
            edges.append([build[1], i])

        # Sort edges by non-decreasing order.
        edges.sort()

        # Initailize an empty Priority Queue 'live' to store all the
        # newly added buildings, an empty list answer to store the skyline key points.
        live, answer = [], []
        idx = 0

        # Iterate over all the sorted edges.
        while idx < len(edges):

            # Since we might have multiple edges at same x,
            # Let the 'curr_x' be the current position.
            curr_x = edges[idx][0]

            # While we are handling the edges at 'curr_x':
            while idx < len(edges) and edges[idx][0] == curr_x:
                # The index 'b' of this building in 'buildings'
                b = edges[idx][1]

                # If this is a left edge of building 'b', we
                # add (height, right) of building 'b' to 'live'.
                if buildings[b][0] == curr_x:
                    right = buildings[b][1]
                    height = buildings[b][2]
                    heapq.heappush(live, [-height, right])

                # If the tallest live building has been passed,
                # we remove it from 'live'.
                while live and live[0][1] <= curr_x:
                    heapq.heappop(live)
                idx += 1

            # Get the maximum height from 'live'.
            max_height = -live[0][0] if live else 0

            # If the height changes at this curr_x, we add this
            # skyline key point [curr_x, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([curr_x, max_height])

        # Return 'answer' as the skyline.
        return answer


class Solution2:
    # O(N^2) Time | O(N) Space
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        positions = set()
        for building in buildings:
            for x in building[:2]:
                positions.add(x)

        positions = sorted(list(positions))

        edge_idx_map = {val: idx for idx, val in enumerate(positions)}
        heights = [0] * len(positions)

        for left, right, height in buildings:
            left_idx = edge_idx_map[left]
            right_idx = edge_idx_map[right]

            for i in range(left_idx, right_idx):
                heights[i] = max(heights[i], height)

        skyline = []

        for idx, height in enumerate(heights):
            curr_x = positions[idx]

            if not skyline or skyline[-1][1] != height:
                skyline.append([curr_x, height])

        return skyline


# DOES NOT WORK - 13/40 test cases.
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        def merge_heights():
            stack = [buildings[0]]

            for building in buildings[1:]:
                curr_building_height = building[2]
                top_stack_height = stack[-1][2]

                if curr_building_height == top_stack_height:
                    continue

                stack.append(building)

            return stack

        merged_buildings = merge_heights()

        first_building = merged_buildings[0]
        first_building_coords = [first_building[0], first_building[2]]
        skyline = [first_building_coords]

        size = len(merged_buildings)
        for i in range(1, size):
            prev_building = merged_buildings[i - 1]
            curr_building = merged_buildings[i]

            is_empty_space = curr_building[0] > prev_building[1]
            is_going_up = curr_building[2] > prev_building[2]
            is_going_down = curr_building[2] < prev_building[2]
            key_point = []

            if is_empty_space:
                key_point = [prev_building[1], 0]
                is_going_up = True
                is_going_down = False

                skyline.append(key_point)

            if is_going_up:
                key_point = [curr_building[0], curr_building[2]]

            elif is_going_down:

                x_key = prev_building[1]
                key_point = [x_key, curr_building[2]]

            skyline.append(key_point)

        last_key_point = [buildings[-1][1], 0]
        skyline.append(last_key_point)

        return skyline


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()

    buildings = [[2, 9, 10],
                 [3, 7, 15],
                 [5, 12, 12],
                 [15, 20, 10],
                 [19, 24, 8]]

    sol2.getSkyline(buildings)

    # output = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    # print(sol.getSkyline(buildings))
    # print(output)

    # buildings = [[0, 2, 3], [2, 5, 3]]
    # output = [[0, 3], [5, 0]]
    # print(sol.getSkyline(buildings))
    # print(output)
