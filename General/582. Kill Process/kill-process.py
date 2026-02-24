from collections import defaultdict, deque
from typing import List


class Solution:
    # O(N) Time | O(N) Space
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        hashmap = defaultdict(list)

        for i in range(len(ppid)):
            if ppid[i] == 0:
                continue

            temp = hashmap[ppid[i]]
            temp.append(pid[i])

            hashmap[ppid[i]] = temp

        queue = deque([kill])
        dead_nodes = []
        while queue:
            node = queue.popleft()
            dead_nodes.append(node)

            if node in hashmap:
                for id in hashmap[node]:
                    queue.append(id)

        return dead_nodes


if __name__ == '__main__':
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5

    sol = Solution().killProcess(pid, ppid, kill)
