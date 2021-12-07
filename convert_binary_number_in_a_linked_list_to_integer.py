"""
LeetCode :: December 2021 Challenge :: 1290. Convert Binary Number in a Linked List to Integer
"""


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        node = head
        while node:
            # result << 1
            result *= 2
            result += node.val
            node = node.next
        return result
