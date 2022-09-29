from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_position = alphabet.index('a') - 1 % 26

        s = list(s)
        for start, end, direction in shifts:

            if direction == 0:
                for i in range(start, end + 1):
                    letter = s[i]
                    new_position = (alphabet.index(letter) - 1) % 26
                    s[i] = alphabet[new_position]
            elif direction == 1:
                for i in range(start, end + 1):
                    letter = s[i]
                    new_position = (alphabet.index(letter) + 1) % 26
                    s[i] = alphabet[new_position]

        return ''.join(s)


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        indexes = [[i, 0]for i in range(len(s))]

        for start, end, direction in shifts:
            for i in range(start, end + 1):
                indexes[i][1] += 1 if direction else -1

        s = list(s)

        for idx, moves in indexes:
            new_position = ((ord(s[idx]) - 97) + moves) % 26
            s[idx] = alphabet[new_position]

        return ''.join(s)



if __name__ == '__main__':
    sol = Solution()
    s = "abc"

    shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    print(sol.shiftingLetters(s, shifts))

    s = "dztz"
    shifts = [[0,0,0],[1,1,1]]
    print(sol.shiftingLetters(s, shifts))
