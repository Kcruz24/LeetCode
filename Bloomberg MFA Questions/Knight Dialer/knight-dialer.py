from math import dist
from traceback import print_exc


class Solution:
    def knightDialerM(self, n: int) -> int:
        if n == 1:
            return 10

        num_pad = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        jumps = set()

        # Jumps
        for _ in range(n-1):
            new_jumps = set()
            for src_key in range(10):
                str_knight_arr = [str(src_key)]
                for dst_key in num_pad[src_key]:
                    str_knight_arr.append(str(dst_key))
                    if ''.join(str_knight_arr) in jumps:
                        return len(jumps)

                    full_digit = ''.join(str_knight_arr)
                    new_jumps.add(full_digit)
                    if len(str_knight_arr) == n:
                        str_knight_arr.pop()

            jumps = new_jumps
        print(sorted(jumps))
        print('hey')
        return len(jumps)

    def knightDialer(self, n):
        # Neighbors maps K: starting_key -> V: list of possible destination_keys

        neighbors = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }

        # 0: 2
        # 4: 3
        # 6: 3

        default_num_pad = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        jumps = n - 1

        # Jumps
        for _ in range(jumps):
            num_pad = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for key in neighbors:
                for value in neighbors[key]:
                    num_pad[value] = (num_pad[value] + default_num_pad[key]) % (10**9 + 7)
            default_num_pad = num_pad

        return sum(default_num_pad) % (10**9 + 7)

# https://leetcode.com/problems/knight-dialer/discuss/189287/O(n)-time-O(1)-space-DP-solution-+-Google-interview-question-writeup


if __name__ == '__main__':
    sol = Solution()

    n = 4

    print(sol.knightDialer(n))
