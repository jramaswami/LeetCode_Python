"""
LeetCode
3161. Block Placement Queries
May 2026 Challenge
jramaswami
"""


from typing import List
import sortedcontainers


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        soln = []
        obstacles = sortedcontainers.SortedList()
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])
            else:
                soln.append(False)
                x = q[1]
                sz = q[2]
                prev = 0
                for curr in obstacles:
                    if prev >= x:
                        break
                    curr = min(curr, x)
                    dist = curr - prev
                    if dist >= sz:
                        soln[-1] = True
                        break
                    prev = curr
        return soln


def test_1():
    queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
    expected = [False,True,True]
    assert Solution().getResults(queries) == expected


def test_2():
    queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
    expected = [True, True,False]
    assert Solution().getResults(queries) == expected


def test_437():
    "WA"
    queries = [[2,1,1]]
    expected = [True]
    assert Solution().getResults(queries) == expected