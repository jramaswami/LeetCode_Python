"""
LeetCode :: February 2022 Challenge :: 23. Merge k Sorted Lists
jramaswami
"""


import heapq


class HItem:
    "Wrapper for queue item to get the < operator."
    def __init__(self, first):
        self.key = first.val
        self.node = first

    def __lt__(self, other):
        return self.key < other.key


class Solution:
    def mergeKLists(self, lists):
        queue = []
        for first in lists:
            if first:
                heapq.heappush(queue, HItem(first))

        head = ListNode()
        curr = head

        while queue:
            item = heapq.heappop(queue)
            curr.next = item.node
            first = item.node.next
            if first:
                heapq.heappush(queue, HItem(first))
            curr = curr.next
            curr.next = None

        return head.next
