"""
LeetCode
3161. Block Placement Queries
May 2026 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=rHlO09AkA_g
"""


from typing import List
import sortedcontainers


MX = pow(10, 5)


class SegmentTree:
    def __init__(self):
        self.st = [0] * (4 * (MX+1))

    def insert(self, idx, val, node=1, left=0, right=MX):
        if left == right:
            self.st[node] = val
        else:
            mid = left + (right - left) // 2
            if idx <= mid:
                self.insert(idx, val, node*2, left, mid)
            else:
                self.insert(idx, val, node*2 + 1, mid+1, right)
            self.st[node] = max(self.st[node*2], self.st[node*2+1])

    def check(self, query_left, query_right, node = 1, left = 0, right = MX):
        if right < query_left or left > query_right:
            return 0
        if query_left <= left and query_right >= right:
            return self.st[node]
        mid = left + (right - left) // 2
        return max(
            self.check(query_left, query_right, node*2, left, mid),
            self.check(query_left, query_right, node*2+1, mid+1, right)
        )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        soln = []
        obstacles = sortedcontainers.SortedList([0, MX])
        st = SegmentTree()
        st.insert(0, MX)
        for q in queries:
            if q[0] == 1:
                _, x = q
                i = obstacles.bisect_left(x)
                left, right = obstacles[i-1], obstacles[i]
                st.insert(left, x-left)
                st.insert(x, right - x)
                obstacles.add(x)
            else:
                _, x, sz = q
                i = obstacles.bisect_left(x)
                left, right = 0, obstacles[i-1]
                prev = st.check(left, right-1)
                tail = x - right
                mx = max(prev, tail)
                soln.append(mx >= sz)
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


def test_484():
    "WA"
    queries = [[2,1,2]]
    expected = [False]
    assert Solution().getResults(queries) == expected


def test_689():
    "WA"
    queries = [[1,1],[2,4,3]]
    expected = [True]
    assert Solution().getResults(queries) == expected