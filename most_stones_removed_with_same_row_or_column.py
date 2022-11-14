"""
LeetCode :: 947. Most Stones Removed with Same Row or Column
November 2022 Challenge
jramaswami
"""


from typing import *
import collections


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        by_col = collections.defaultdict(list)
        by_row = collections.defaultdict(list)
        for r, c in stones:
            by_col[c].append(r)
            by_row[r].append(c)

        def bfs(init_r, init_c, visited):
            queue = collections.deque()
            queue.append((init_r, init_c))
            visited.add((init_r, init_c))
            while queue:
                r0, c0 = queue.popleft()
                # row neighbors
                for r1 in by_col[c0]:
                    if (r1, c0) not in visited:
                        visited.add((r1, c0))
                        queue.append((r1, c0))
                # col neighbors
                for c1 in by_row[r0]:
                    if (r0, c1) not in visited:
                        visited.add((r0, c1))
                        queue.append((r0, c1))

        soln = 0
        visited = set()
        for r, c in stones:
            if (r, c) not in visited:
                soln += 1
                bfs(r, c, visited)
        return len(stones) - soln



def test_1():
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    expected = 5
    assert Solution().removeStones(stones) == expected


def test_2():
    stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    expected = 3
    assert Solution().removeStones(stones) == expected


def test_3():
    stones = [[0,0]]
    expected = 0
    assert Solution().removeStones(stones) == expected
