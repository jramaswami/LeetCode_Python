"""
LeetCode
2127. Maximum Employees to Be Invited to a Meeting
January 2025 Challenge
jramaswami

Thank You NeetCodeIO!
"""


import collections
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Find the longest cycle.
        longest_cycle = 0
        visited = [False for _ in favorite]
        length_2_cycles = []
        for i, _ in enumerate(favorite):
            if not visited[i]:
                start, curr = i, i
                curr_set = set()
                while not visited[curr]:
                    visited[curr] = True
                    curr_set.add(curr)
                    curr = favorite[curr]

                # Curr points to cycle.
                if curr in curr_set:
                    # New cycle.
                    cycle_length = len(curr_set)
                    # Remove nodes before cycle.
                    while start != curr:
                        cycle_length -= 1
                        start = favorite[start]
                    longest_cycle = max(longest_cycle, cycle_length)
                    if cycle_length == 2:
                        length_2_cycles.append([curr, favorite[curr]])
        
        # Find the longest non closed circles.
        reverse_graph = collections.defaultdict(list)
        for dst, src in enumerate(favorite):
            reverse_graph[src].append(dst)

        def bfs(root, pair):
            result = 0
            queue = collections.deque()
            queue.append((root, 0))
            while queue:
                u, d = queue.popleft()
                if u != pair:
                    result = max(result, d)
                    for v in reverse_graph[u]:
                        queue.append((v, d+1))
            return result

        chain_sum = 0
        for root1, root2 in length_2_cycles:
            chain_sum += bfs(root1, root2) + bfs(root2, root1) + 2
        return max(chain_sum, longest_cycle)




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
