class Solution:
    # O(N) Time | O(N) Space
    def isValid(self, s: str) -> bool:
        map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for p in s:
            is_open_parentheses = p in map

            if stack and is_open_parentheses and stack[-1] == map[p]:
                stack.pop()
            else:
                stack.append(p)

        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()

    s = '()'
    print(sol.isValid(s))

    s = '()[]{}'
    print(sol.isValid(s))

    s = '(]'
    print(sol.isValid(s))
