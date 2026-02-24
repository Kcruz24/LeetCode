
'''
- '()' -> Balanced
- AB == '()()' -> 2
- (A) == 2 * A

()

()()()()()
()
Steps:
    1. Keep track of the simple valid parentheses -> '()' and A + B
    2. Keep track of the depth
    3. Calculate depth and add the result to our running counter variable
'''


#
class Solution:
    # O(N) Time | O(N) Space
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        stack = []
        max_depth = 0
        open_parentheses = '('

        # count = 2
        for parentheses in s:
            if stack and stack[-1] == open_parentheses:
                max_depth += 1

            if not stack and max_depth > 0:
                count += 2 * max_depth

            if parentheses == open_parentheses:
                stack.append(parentheses)
            else:
                count += 1
                stack.pop()

        return count


class Solution2:
    # O(N) Time | O(N) Space
    def scoreOfParentheses(self, s):
        stack = [0]
        open_parentheses = '('

        for parentheses in s:
            if parentheses == open_parentheses:
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] += max(2 * score, 1)

        final_score = stack.pop()
        return final_score


if __name__ == '__main__':
    sol = Solution2()

    s = '()'
    print(sol.scoreOfParentheses(s))

    s = '(())'
    print(sol.scoreOfParentheses(s))

    s = '()()'
    print(sol.scoreOfParentheses(s))
