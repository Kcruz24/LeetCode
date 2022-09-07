# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(max(N, M)) Time | O(max(N, M)) Space
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            trav = head
            trav2 = trav

            while trav:
                trav = trav.next
                trav2.next = prev

                prev = trav2
                trav2 = trav

            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        result = ListNode(0)
        trav = result
        carry_over = 0

        while l1 or l2 or carry_over:
            digit_one = l1.val if l1 else 0
            digit_two = l2.val if l2 else 0

            sum_of_values = digit_one + digit_two + carry_over

            carry_over, new_digit = divmod(sum_of_values, 10)

            new_node = ListNode(new_digit)
            trav.next = new_node

            l1 = l1.next if l1.next else None
            l2 = l2.next if l2.next else None
            trav = trav.next

        result.next = reverse(result.next)
        return result.next
