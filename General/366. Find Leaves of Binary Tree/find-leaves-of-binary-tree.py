from collections import defaultdict
class Solution:
    # O(N) time | O(N) space
    def findLeaves(self, root):
        leaves_map = defaultdict(list)
        _ = self.dfs(root, leaves_map)
        res = []
        for i in range(len(leaves_map)):
            res.append(leaves_map[i + 1])

        return res

    def dfs(self, root, hashMap):
        if root is None:
            return 0

        left = self.dfs(root.left, hashMap)
        right = self.dfs(root.right, hashMap)

        runningHeight = 1 + max(left, right)
        hashMap[runningHeight].append(root.val)
        return runningHeight

