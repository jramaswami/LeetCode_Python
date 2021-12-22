"""
LeetCode :: December 2021 Challenge :: 143. Reorder List
jramaswami
"""


import collections


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        nodes = collections.deque()
        while curr:
            nodes.append(curr)
            curr = curr.next
            nodes[-1].next = None

        dummy = ListNode()
        curr = dummy
        i = 0
        while nodes:
            if i % 2:
                curr.next = nodes.pop()
            else:
                curr.next = nodes.popleft()
            curr = curr.next
            i += 1
        return dummy.next
