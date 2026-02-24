class Solution:
    # O(N) Time | O(1) Space
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            x = str(x)
            self.delete_zeroes(x)

            x = int(x[::-1])
            x = -x

        else:
            x = str(x)
            self.delete_zeroes(x)

            x = int(x[::-1])

        if x < pow(-2, 31) or x > (pow(2, 31) - 1) - 1:
            return 0

        return x

    def delete_zeroes(self, x):
        if '0' in x:
            x.replace('0', '')


if __name__ == '__main__':
    sol = Solution()

    x = 123
    print(sol.reverse(x))

    x = -123
    print(sol.reverse(x))

    x = 120
    print(sol.reverse(x))
