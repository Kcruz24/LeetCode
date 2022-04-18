class Solution:
    # O(N) time | O(1) space
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0

        for char in s:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1

            maxDepth = max(maxDepth, depth)

        return maxDepth


if __name__ == '__main__':
    s = "(1+(2*3)+((8)/4))+1"

    sol = Solution()

    print(sol.maxDepth(s))
