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


class Solution:
    # O(N) Time | O(1) Space
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        while fast < len(chars):

            chars[slow] = chars[fast]
            count = 1

            while fast + 1 < len(chars) and chars[fast] == chars[fast+1]:
                fast += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[slow+1] = c
                    slow += 1

            fast += 1
            slow += 1

        return slow
