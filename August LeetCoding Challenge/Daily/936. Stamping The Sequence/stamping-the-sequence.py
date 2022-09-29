from collections import deque
from typing import List


class Solution:
    # O(N(N - M)) Time | O(N(N - M)) Space - Where "M" and "N" are the lengths
    # of stamp and target.
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_length = len(stamp)
        target_length = len(target)

        queue = deque()
        done = [False] * target_length
        ans = []
        needs_to_change = []

        for i in range(target_length - stamp_length + 1):
            made = set()
            todo = set()

            for j, stamp_char in enumerate(stamp):
                target_char = target[i + j]
                if target_char == stamp_char:
                    made.add(i + j)
                else:
                    todo.add(i + j)

            needs_to_change.append((made, todo))

            if not todo:
                ans.append(i)

                for j in range(i, i + stamp_length):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        while queue:
            char_idx = queue.popleft()

            start = max(0, char_idx - stamp_length + 1)
            end = min(target_length - stamp_length, char_idx) + 1

            for j in range(start, end):
                if char_idx not in needs_to_change[j][1]:
                    continue

                needs_to_change[j][1].discard(char_idx)

                if needs_to_change[j][1]:
                    continue

                ans.append(j)

                for m in needs_to_change[j][0]:
                    if done[m]:
                        continue

                    queue.append(m)
                    done[m] = True

        if all(done):
            return ans[::-1]

        return []


class Solution:
    def equals(self, target, stamp, i):

        for j, c in enumerate(stamp):
            if not (target[i + j] == c or target[i + j] == '?'):
                return False

        return True

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = [c for c in target]

        N, M = len(target), len(stamp)
        ans = []
        already_in = set()

        for i in range(N - M + 1):

            if self.equals(target, stamp, i):
                for x in range(i, -1, -1):
                    if x in already_in:
                        break

                    already_in.add(x)

                    if self.equals(target, stamp, x):
                        ans.append(x)
                        target[x:x+M] = ['?'] * M

        return ans[::-1] if all([c == '?' for c in target]) else []
