"""
LeetCode :: December 2021 Challenge :: 116. Populating Next Right Pointers in Each Node
jramaswami
"""


import collections


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        queue = collections.deque()
        levels = []
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node:
                if len(levels) <= level:
                    levels.append([])
                levels[level].append(node)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        for level in levels:
            for a, b in zip(level[:-1], level[1:]):
                a.next = b
            level[-1].next = None

        return root
