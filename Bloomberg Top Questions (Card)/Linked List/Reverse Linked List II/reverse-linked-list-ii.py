# From LeetCode
# Solution
class Solution2:
    def reverseBetween(self, head, left, right):
        if not head:
            return None

        trav = head
        prev = None

        # Move the two pointers until they reach the proper starting point
        # in the list
        while left > 1:
            prev = trav
            trav = trav.next
            left -= 1
            right -= 1

        # The two pointers that will fix the final connections
        tail_prev = prev
        tail = trav

        while right:
            next_node = trav.next
            trav.next = prev
            prev = trav
            trav = next_node
            right -= 1

        if tail_prev:
            tail_prev.next = prev
        else:
            head = prev

        tail.next = trav
        return head
