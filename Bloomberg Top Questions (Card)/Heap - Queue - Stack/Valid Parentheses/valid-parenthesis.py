class Solution:
    # O(N) Time | O(1) Space
    def isValid(self, s):
        stack = []

        parenthesis_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in parenthesis_map:
                top = stack.pop() if stack else None

                if parenthesis_map[char] != top:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
