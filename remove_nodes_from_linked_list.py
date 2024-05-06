"""
LeetCode
2487. Remove Nodes From Linked List
May 2024 Challenge
jramaswami
"""


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recurse to remove returning both the prev node and the curr max.

        def rec(node):
            if node is None:
                return None, 0

            prev_node, prev_max = rec(node.next)
            node.next = prev_node
            if node.val < prev_max:
                return prev_node, prev_max
            else:
                return node, node.val

        return rec(head)[0]