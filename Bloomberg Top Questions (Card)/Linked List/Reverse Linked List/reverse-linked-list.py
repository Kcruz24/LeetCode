from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(N) Time | O(1) Space
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev = None
        trav = head

        while trav:
            nextNode = trav.next
            trav.next = prev
            prev = trav
            trav = nextNode

        return prev
