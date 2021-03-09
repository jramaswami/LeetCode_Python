"""
LeetCode :: 206. Reverse Linked List
jramaswami
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = follow = head
        while curr:
            follow = curr.next
            curr.next = prev
            prev = curr
            curr = follow
        return prev
