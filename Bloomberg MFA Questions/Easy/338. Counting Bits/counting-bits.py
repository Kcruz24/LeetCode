from typing import List


class Solution:
    # O(N^2) Time | O(N) Space
    def countBits(self, n: int) -> List[int]:
        output = []
        total = 0

        for i in range(n + 1):
            converted_num = list(bin(i))
            convert_to_int = [int(num) for num in converted_num[2:]]

            total = sum(convert_to_int)
            output.append(total)

        return output


if __name__ == '__main__':
    sol = Solution()
    n = 2

    print(sol.countBits(n))
