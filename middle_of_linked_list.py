"""
LeetCode :: December 2021 Challenge :: 876. Middle of the Linked List
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
