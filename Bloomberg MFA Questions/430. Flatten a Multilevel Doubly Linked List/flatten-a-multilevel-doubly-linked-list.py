# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, next):
        self.val = val
        self.prev = None
        self.next = next
        self.child = None


# Iterative
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


# Recursive
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


# In-Place
class Solution3(object):
    # O(N) Time | O(1) Space
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # traverse the list and look for nodes, where self.child is not None
        # keep the pointer to the previous node and to the original next node
        # merge a child list to the parent list - connect prev and next pointers
        # continue traversing until encountering another node where self.child is not None,
        # or reaching the end of the main list

        current = head

        while current is not None:
            # check for child node
            if current.child is not None:
                # merge child list into the parent list
                self.merge(current)

            # move to the next node
            current = current.next

        return head

    def merge(self, current):
        child = current.child

        # traverse child list until we get the last node
        while child.next is not None:
            child = child.next

        # child is now pointing at the last node of the child list
        # we need to connect child.next to current.next, if there is any
        if current.next is not None:
            child.next = current.next
            current.next.prev = child

        # now, we have to connect current to the child list
        # child is currently pointing at the last node of the child list,
        # so we need to use pointer (current.child) to get to the first node of the child list
        current.next = current.child
        current.child.prev = current

        # at the end remove self.child pointer
        current.child = None
