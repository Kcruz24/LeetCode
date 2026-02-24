class Solution:
    # O(Nlog(N)) Time | O(N)
    def getKth(self, lo: int, hi: int, k: int) -> int:
        pairs_powers = []

        for x in range(lo, hi + 1):
            power = self.pow_number(x)
            pairs_powers.append((power, x))

        pairs_powers.sort()

        kth_power = pairs_powers[k - 1][1]
        return kth_power

    def pow_number(self, x):
        steps = 0
        while x != 1:

            if x % 2 == 0:
                x /= 2

            elif x % 2 == 1:
                x = x * 3 + 1

            steps += 1

        return steps


if __name__ == '__main__':
    sol = Solution()

    lo = 7
    hi = 11
    k = 4

    print(sol.getKth(lo, hi, k))
