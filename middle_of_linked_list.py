"""
LeetCode
876. Middle of the Linked List
December 2022 Challenge
jramaswami
"""


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
        return slow
