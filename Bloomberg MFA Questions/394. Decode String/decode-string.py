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


class Solution:
    # O(N) Time | O(N) Space
    def decodeString(self, s: str) -> str:

        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return ''.join(stack)

if __name__ == '__main__':
    sol = Solution()

    string = '3[a2[c]]'
    print(sol.decodeString(string))
