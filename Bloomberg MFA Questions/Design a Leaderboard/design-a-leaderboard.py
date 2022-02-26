# O(NLog(N)) time | O(N) space
class Leaderboard:

    def __init__(self):
        self.leaderboard = {}

    # O(1) time | O(1) space
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.leaderboard:
            self.leaderboard[playerId] += score
        else:
            self.leaderboard[playerId] = score

    # O(NLog(N)) time | O(1) space
    def top(self, K: int) -> int:
        sorted_leaderboard = sorted(self.leaderboard.values(), reverse=True)
        score_sum = 0

        for i in range(K):
            score_sum += sorted_leaderboard[i]

        return score_sum

    # O(N) time | O(1) space
    def reset(self, playerId: int) -> None:
        del self.leaderboard[playerId]


leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]]

hashMap = {}

for i, y in leaderboard:
    hashMap[i] = y

sortedMap = sorted(hashMap.values(), reverse=True)

for i in sortedMap:
    print(i)


if __name__ == '__main__':
    leaderboard = Leaderboard()

    leaderboard.addScore(1, 73)
    leaderboard.addScore(2, 56)
    leaderboard.addScore(3, 39)
    leaderboard.addScore(4, 51)
    leaderboard.addScore(5, 4)

    print(leaderboard.top(1))

    leaderboard.reset(1)
    leaderboard.reset(2)

    leaderboard.addScore(2, 51)

    print(leaderboard.top(3))

