'''
# O(N)


1 -> 2 -> 3 -> 4 -> 5

(5 - 2 = 3

1 <- 2 <- 3 <- 4 <- 5
|

n = 2

'''
from typing import Optional
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # O(N) Time | O(1) Space
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return

        def get_size():
            size_ptr = head
            size = 0

            while size_ptr:
                size += 1
                size_ptr = size_ptr.next

            return size

        def find_node_to_remove():
            nonlocal prev
            size = get_size()

            nth = size - n
            while trav and nth > 0:
                prev = trav
                trav = trav.next
                nth -= 1

        def remove():
            nonlocal head
            if prev:
                prev.next = trav.next
                trav.next = None
            else:
                head = head.next


        prev = None
        trav = head

        find_node_to_remove()
        remove()

        return head
