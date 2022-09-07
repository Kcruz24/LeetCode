from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# AlgoExpert Solution
class Solution:
    # O(N + M) Time | O(1) Space
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return

        if list1 and list2 is None:
            return list1
        elif list2 and list1 is None:
            return list2

        trav_one = list1
        trav_two = list2

        prev_one = None

        while trav_one and trav_two:
            if trav_one.val < trav_two.val:
                prev_one = trav_one
                trav_one = trav_one.next
            else:
                if prev_one:
                    prev_one.next = trav_two

                prev_one = trav_two
                trav_two = trav_two.next
                prev_one.next = trav_one

            if trav_one is None:
                prev_one.next = trav_two

        return list1 if list1.val < list2.val else list2


# LeetCode Solution
class Solution2:
    def mergeTwoLists(self, list1, list2):
        prehead = ListNode(-1)

        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next

            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        prev.next = list1 if list1 is not None else list2

        return prehead.next
