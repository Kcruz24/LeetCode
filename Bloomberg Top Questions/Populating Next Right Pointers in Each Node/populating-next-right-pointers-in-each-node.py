
# Definition for a Node.
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # O(N) time | O(1) space
    def connect(self, root: Node) -> Node:
        head = root

        while head and head.left:
            left_most = head.left

            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left
                head = head.next

            head = left_most

        return root
