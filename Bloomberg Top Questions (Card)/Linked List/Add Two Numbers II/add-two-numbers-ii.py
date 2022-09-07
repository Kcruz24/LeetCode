class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    # O(max(N, M)) Time | O(max(N, M)) Space
    def addTwoNumbers(self, list1, list2):
        list1_reversed = self.reverse(list1)
        list2_reversed = self.reverse(list2)

        result = ListNode(0)
        trav = result

        carry_over = 0

        while list1_reversed or list2_reversed or carry_over != 0:
            value1 = list1_reversed.val if list1_reversed else 0
            value2 = list2_reversed.val if list2_reversed else 0

            sum_of_values = value1 + value2 + carry_over

            carry_over = sum_of_values % 10

            new_node = ListNode(carry_over)
            trav.next = new_node

            carry_over = sum_of_values // 10

            list1_reversed = list1_reversed.next if list1_reversed else None
            list2_reversed = list2_reversed.next if list2_reversed else None
            trav = trav.next

        # Eliminate leading zero
        result = result.next

        result_reversed = self.reverse(result)
        return result_reversed.next

    # O(N) Time | O(1) Space
    def reverse(self, head):
        if not head:
            return

        prev = None
        trav = head

        while trav:
            next_node = trav.next
            trav.next = prev
            prev = trav
            trav = next_node

        return prev

# Two Stacks Solution
# From https://leetcode.com/problems/add-two-numbers-ii/discuss/926807/Python-Two-stacks-solution-explained


class Solution2:
    def addTwoNumbers(self, l1, l2):
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        carry, head = 0, None

        while st1 or st2 or carry:
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new

        return head
