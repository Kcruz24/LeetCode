class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        star = '*'
        i = 1
        while star in s:
            if s[i] == star:
                for _ in range(2):
                    s.pop(i)
                    i -= 1

            i += 1

        return ''.join(s)


# Optimal
class Solution:
    # O(N) Time | O(N) Space
    def removeStars(self, s: str) -> str:
        stack = []
        star = '*'

        for char in s:
            if char == star:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()

    s = "leet**cod*e"
    print(sol.removeStars(s))

    s = "erase*****"
    print(sol.removeStars(s))
