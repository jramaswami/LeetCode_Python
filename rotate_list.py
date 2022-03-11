"""
LeetCode :: March 2022 Challenge :: Rotate List
jramaswami
"""


import collections


class Solution:

    def rotateRight(self, head, k):
        # Boundary case:
        if head is None:
            return head

        nodes = collections.deque()
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        nodes.rotate(k)

        nodes[-1].next = None
        for i, left in enumerate(nodes):
            if i + 1 < len(nodes):
                left.next = nodes[i+1]
            else:
                left.next = None
        return nodes[0]
