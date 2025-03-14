from typing import List


class UnionFind:
    def __init__(self, n):
        self.root = [node for node in range(n)]
        self.rank = [1] * n


    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x

            elif self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y

            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)




class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        uf = UnionFind(26)
        base = 97

        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - base
                y = ord(eq[3]) - base

                uf.union(x, y)

        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - base
                y = ord(eq[3]) - base

                if uf.connected(x, y):
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()

    equations = ["a==b", "b!=a"]
    print(sol.equationsPossible(equations))

    equations = ["b==a","a==b"]
    print(sol.equationsPossible(equations))

    print(ord('a') - ord('a'))
    print(ord('b') - ord('a'))