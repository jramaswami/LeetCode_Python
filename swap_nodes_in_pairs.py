"""
LeetCode :: February 2022 Challenge :: 24. Swap Nodes in Pairs
jramaswami
"""


class Solution:

    def swapPairs(self, head):
        if head is None:
            return head

        def get_next(node):
            if node is None:
                return None
            return node.next

        dummy = ListNode(0, head)
        prev = dummy
        left = head
        right = head.next
        while left and right:
            prev.next, right.next, left.next = right, left, right.next
            prev, left, right = left, get_next(left), get_next(left.next)
        return dummy.next
