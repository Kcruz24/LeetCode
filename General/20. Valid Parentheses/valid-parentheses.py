class Solution:
    # O(N) time | O(N) space
    def isValid(self, s: str) -> bool:
        stack = []

        parenthesis_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in parenthesis_map:
                if stack:
                    top_element = stack.pop()

                if parenthesis_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0