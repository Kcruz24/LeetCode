class Solution:
    # O(log(N)) Time | O(1) Space
    def mirror_reflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p /= 2
            q /= 2

        if q % 2 == 0:
            return 0

        if p % 2 == 0:
            return 2

        return 1


if __name__ == '__main__':
    sol = Solution()

    p = 2
    q = 1

    print(sol.mirror_reflection(p, q))
