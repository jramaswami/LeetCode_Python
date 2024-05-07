"""
LeetCode
2816. Double a Number Represented as a Linked List
May 2024 Challenge
jramaswami
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rec(node):
            if node is None:
                return 0, None

            carry, prev_node = rec(node.next)
            new_carry, new_val = divmod(carry + (node.val * 2), 10)
            new_node = ListNode(new_val, prev_node)
            return new_carry, new_node

        carry, new_head = rec(head)
        if carry:
            return ListNode(carry, new_head)
        return new_head