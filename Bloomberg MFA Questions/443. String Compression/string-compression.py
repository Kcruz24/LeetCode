from typing import List


class Solution:
    # O(N) time | O(1)
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        s = ''
        counter = 1

        for i in range(1, len(chars)):
            prev_char = chars[i - 1]
            curr_char = chars[i]

            if prev_char == curr_char:
                counter += 1
            else:
                s += prev_char + str(counter) if counter > 1 else prev_char
                counter = 1

        s += chars[-1] + str(counter) if counter > 1 else chars[-1]

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)
