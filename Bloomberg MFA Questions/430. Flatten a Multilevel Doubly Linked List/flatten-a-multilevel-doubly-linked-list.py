# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, next):
        self.val = val
        self.prev = None
        self.next = next
        self.child = None


class Solution:
    # O(N) time | O(N) space
    # Runtime: 24 ms, Faster than 99.41% of python solutions
    def flatten(self, head):
        if not head:
            return

        prev = None
        stack = [head]

        while stack:
            curr = stack.pop()

            if prev:
                prev.next = curr
                curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        return head


class Solution2:
    # O(N) time | O(N) space
    # Runtime: 24 ms, Faster than 99.25% of python solutions
    def flatten(self, head: Node) -> Node:
        # define self.prev as global variant
        self.prev = None
        self.dfs(head)
        return head

    def dfs(self, cur: Node):
        if not cur:
            return

        # At first, self.prev is none
        if self.prev:
            cur.prev = self.prev
            self.prev.next = cur

        self.prev = cur
        # since the next node has been changed after dfs, we need to keep the original next node
        next = cur.next

        self.dfs(next)
        self.dfs(cur.child)
        # after we have traversed the cur.child, we need to set cur.child is None
        cur.child = None
