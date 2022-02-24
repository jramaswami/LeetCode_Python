"""
LeetCode :: February 2022 Challenge :: 148. Sort List
jramaswami
"""


class Solution:

    def sortList(self, head):
        if head is None:
            return None
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        nodes.sort(key=lambda node: node.val)
        nodes.append(None)
        for left, right in zip(nodes[:-1], nodes[1:]):
            left.next = right
        return nodes[0]
