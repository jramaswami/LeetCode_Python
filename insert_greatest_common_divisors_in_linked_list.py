"""
LeetCode
2807. Insert Greatest Common Divisors in Linked List
September 2024 Challenge
jramaswami
"""


import math


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Turn linked list into list
        curr = head
        L = []
        while curr is not None:
            L.append(curr.val)
            curr = curr.next
        # Create new linked list with gcds
        dummy = ListNode()
        curr = dummy
        G = []
        for a, b in zip(L[:-1], L[1:]):
            g = math.gcd(a, b)
            a0 = ListNode(a)
            g0 = ListNode(g)
            curr.next = a0
            a0.next = g0
            curr = g0
        # Add the last node
        curr.next = ListNode(L[-1])
        return dummy.next
