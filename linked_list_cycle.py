"""
LeetCode :: Linked List Cycle
jramaswami
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        while True:
            if fast.next is None:
                return False
            fast = fast.next.next
            if fast is None:
                return False
            slow = slow.next
            if slow == fast:
                return True
