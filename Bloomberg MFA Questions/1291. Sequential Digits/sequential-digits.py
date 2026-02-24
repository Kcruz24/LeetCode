from typing import List


class Solution:
    # O(1) Time | O(1) Space
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = '123456789'
        n = 10
        nums = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])

                if num >= low and num <= high:
                    nums.append(num)

        return nums


class Solution:
    def sequentialDigits(self, low, high):
        ans = []

        def backtrack(path, pathInt):
            if pathInt > high:
                return
            if low <= pathInt <= high:
                ans.append(pathInt)
            if not path:
                for i in range(1, 10):
                    backtrack(str(i), i)
                else:
                    lastDigit = int(path[-1])
                    if lastDigit == 9:
                        return

                    newDigitString = path + str(lastDigit + 1)
                    backtrack(newDigitString, pathInt * 10 + (lastDigit + 1))

        backtrack('', 0)
        ans.sort()
        return ans


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        def dfs(cur, digit):
            if digit <= 10 and low <= cur <= high:
                ans.append(cur)
            elif cur < low:
                pass
            else:
                return

            cur = cur * 10 + digit
            dfs(cur, digit + 1)

        ans = []
        for i in range(1, 10):
            dfs(0, i)

        return sorted(ans)


if __name__ == '__main__':
    sol = Solution()

    low = 100
    high = 300
    print(sol.sequentialDigits(low, high))

    low = 1000
    high = 13000
    print(sol.sequentialDigits(low, high))
