"""
LeetCode
206. Reverse Linked List
March 2023 Challenge
jramaswami
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        dummy = ListNode(0)

        def rec(node):
            if node is None:
                return dummy

            prev = rec(node.next)
            prev.next = node
            node.next = None
            return node

        rec(head)
        return dummy.next
