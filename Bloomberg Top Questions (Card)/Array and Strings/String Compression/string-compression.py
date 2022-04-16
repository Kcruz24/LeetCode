from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        s = ''
        counter = 1
        prev = 0
        curr = 1

        while curr < len(chars):
            prev_char = chars[prev]
            curr_char = chars[curr]

            if prev_char == curr_char:
                counter += 1

            if prev_char != curr_char:
                s += prev_char + str(counter) if counter > 1 else prev_char
                counter = 1

            prev += 1
            curr += 1

        s += chars[prev] + str(counter) if counter > 1 else chars[prev]

        for i in range(len(s)):
            chars[i] = s[i]

        new_length = len(chars[:len(s)])
        print(chars[:len(s)])
        return new_length


if __name__ == '__main__':
    sol = Solution()
    chars = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
    chars2 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    chars3 = ["a"]
    chars4 = ['a', 'b', 'c']

    print(sol.compress(chars))
    print(sol.compress(chars2))
    print(sol.compress(chars3))
    print(sol.compress(chars4))
