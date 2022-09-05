'''

s = 'a)b(c)d'
output = 'ab(c)d'

parenthesis = [(')', 1), ]
stack = ['a', ')', 'b', '(']


'''


class Solution:
    # O(N) Time | O(N) Space
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        parenthesis = '()'

        for idx, letter in enumerate(s):
            if letter not in parenthesis:
                continue

            if letter == '(':
                stack.append(idx)
            elif not stack:
                indexes_to_remove.add(idx)
            else:
                stack.pop()

        for idx in stack:
            indexes_to_remove.add(idx)

        new_string = []
        for idx, char in enumerate(s):
            if idx not in indexes_to_remove:
                new_string.append(char)

        return ''.join(new_string)


if __name__ == '__main__':
    sol = Solution()

    s = "L(e)))et((co)d(e"
    print(sol.minRemoveToMakeValid(s))

    s = 'a)b(c)d'
    print(sol.minRemoveToMakeValid(s))
