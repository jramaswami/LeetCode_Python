"""
LeetCode
1298. Maximum Candies You Can Get from Boxes
June 2025 Challenge
jramaswami

Thank You Larry!
"""


import itertools


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        accessible = [False for _ in status]
        opened = [(s == 1) for s in status]
        visited = [False for _ in status]

        # Add all boxes that are accessible
        for b in initialBoxes:
            accessible[b] = True

        queue = collections.deque()
        for b, _ in enumerate(accessible):
            if accessible[b] and opened[b]:
                queue.append(b)
                visited[b] = True

        soln = 0
        while queue:
            b = queue.popleft()
            soln += candies[b]

            for x in keys[b]:
                opened[x] = True

            for x in containedBoxes[b]:
                accessible[x] = True

            for x in set(itertools.chain(keys[b], containedBoxes[b])):
                if accessible[x] and opened[x] and not visited[x]:
                    queue.append(x)
                    visited[x] = True

        return soln