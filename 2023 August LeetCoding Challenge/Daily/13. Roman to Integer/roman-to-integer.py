
class Solution:
    # O(N) Time | O(1) Space
    def romanToInt(self, s: str) -> int:
        roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        running_sum = 0

        for i in range(len(s) - 1):
            if roman_nums[s[i]] < roman_nums[s[i + 1]]:
                running_sum -= roman_nums[s[i]]
            else:
                running_sum += roman_nums[s[i]]

        running_sum += roman_nums[s[-1]]

        return running_sum


if __name__ == '__main__':
    sol = Solution()

    print(sol.romanToInt('XC'))