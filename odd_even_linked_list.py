"""
LeetCode :: December 2021 Challenge :: 328. Odd Even Linked List
jramaswami
"""


class Solution:

    def oddEvenList(self, head):
        dummy_even = ListNode()
        dummy_odd = ListNode()

        curr_even = dummy_even
        curr_odd = dummy_odd

        curr_node = head
        index = 0
        while curr_node:
            if index % 2:
                # Odd node
                curr_odd.next = curr_node
                curr_node = curr_node.next
                curr_odd = curr_odd.next
                curr_odd.next = None
            else:
                # Even node
                curr_even.next = curr_node
                curr_node = curr_node.next
                curr_even = curr_even.next
                curr_even.next = None
            index += 1

        # curr_even should point to last even node.
        new_head = dummy_even.next
        curr_even.next = dummy_odd.next
        return new_head
