from collections import deque


class Solution:
    # O(N) time | O(D) - where 'D' is the max depth of nested encoding.
    def decodeString(self, s: str) -> str:
        stack = []

        encoded_string = ''
        digit = ''

        for char in s:
            if char.isalpha():
                encoded_string += char
            elif char.isdigit():
                digit += char
            elif char == '[':
                stack.append((encoded_string, digit))
                encoded_string = ''
                digit = ''
            else:
                prev_char, count = stack.pop()

                encoded_string = prev_char + encoded_string * int(count)

        return encoded_string



if __name__ == '__main__':
    sol = Solution()

    string = '3[a2[c]]'
    print(sol.decodeString(string))
