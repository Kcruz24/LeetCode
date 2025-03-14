
'''

symbols = [(1, 'L'), (3, 'R'), (7, 'L'), (8, 'R'), (11, 'L')]
symbols = [(-1, 'L'), (1, 'L'), (3, 'R'), (7, 'L'), (8, 'R'), (11, 'L'), (14, 'R')]
symbols = [(1, 'L'), (3, 'R'), (7, 'L'), (8, 'R'), (11, 'L'), (14, 'R')]

'''


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def cmp(a, b):
            return (a > b) - (a < b)

        symbols = [(idx, char) for idx, char in enumerate(dominoes) if char != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in range(i + 1, j):
                    ans[k] = '.LR'[cmp(k - i, j - k)]

        return ''.join(ans)


if __name__ == '__main__':
    sol = Solution()

    dominoes = '.L.R...LR..L..'
    print(sol.pushDominoes(dominoes))
