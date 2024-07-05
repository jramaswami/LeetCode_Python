"""
LeetCode
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
July 2024 Challenge
jramaswami
"""


import collections


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_critical_point(w):
            if w[0] < w[1] and w[1] > w[2]:
                return True
            if w[0]  > w[1] and w[1] < w[2]:
                return True
            return False

        window = collections.deque()
        critical_points = []
        index = 0
        curr_node = head
        while curr_node:
            window.append(curr_node.val)
            while len(window) > 3:
                window.popleft()
            if len(window) == 3 and is_critical_point(window):
                critical_points.append(index)
            curr_node = curr_node.next
            index += 1
        
        if len(critical_points) > 1:
            min_dist = min(b - a for a, b in zip(critical_points[:-1], critical_points[1:]))
            max_dist = critical_points[-1] - critical_points[0]
            return [min_dist, max_dist]
        return [-1, -1]
