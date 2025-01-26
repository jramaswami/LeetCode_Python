"""
LeetCode
2127. Maximum Employees to Be Invited to a Meeting
January 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Longest cycle or chain
        soln = 0

        # Find cycle using bfs
        visited = set()
        for root, _ in enumerate(favorite):
            if root not in visited:
                visited.add(root)
                queue = collections.deque()
                queue.append((1, root))
                while queue:
                    d, u = queue.popleft()
                    v = favorite[u]
                    if v in visited:
                        # Cycle
                        soln = max(soln, d)
                    else:
                        visited.add(v)
                        queue.append((d+1, v))

        # Reverse the graph to find the end of any chains (zero indegree)
        # Start with those to find chains with bfs
        reverse_graph = collections.defaultdict(list)
        indegree = [0 for _ in favorite]
        for v, u in enumerate(favorite):
            reverse_graph[u].append(v)
            indegree[v] += 1

        for root in (u for u, d in enumerate(indegree) if d == 0):
            # zero indegree is the beginning of a chain
            visited = set()
            queue = collections.deque()
            visited.add(root)
            queue.append((1, root))
            while queue:
                d, u = queue.popleft()
                soln = max(soln, d)
                for v in reverse_graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((d+1, v))

        return soln


def test1():
    favorite = [2,2,1,2]
    expected = 3
    assert Solution().maximumInvitations(favorite) == expected


def test2():
    favorite = [1,2,0]
    expected = 3
    assert Solution().maximumInvitations(favorite) == expected


def test3():
    favorite = [3,0,1,4,1]
    expected = 4
    assert Solution().maximumInvitations(favorite) == expected


def test4():
    "WA"
    favorite = [1,0,0,2,1,4,7,8,9,6,7,10,8]
    expected = 6
    assert Solution().maximumInvitations(favorite) == expected
