"""
LeetCode :: January 2022 Challenge :: 142. Linked List Cycle II
jramaswami
"""


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head
        index = 0
        while curr:
            if curr.next == None:
                return None

            if curr in visited:
                return curr

            visited.add(curr)
            index += 1
            curr = curr.next
