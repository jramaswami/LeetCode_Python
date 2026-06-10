"""
LeetCode
3691. Maximum Total Subarray Value II
June 2026 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=ekNtCTIbBFo
"""


import heapq
import math
from typing import List


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.st = [(0, 0) for _ in range(4 * self.n)]  # (max, min)
        self.build(1, 0, self.n-1)

    def build(self, node, left, right):
        if left == right:
            self.st[node] = (self.arr[left], self.arr[right])
            return
        mid = left + (right - left) // 2
        self.build(2 * node, left, mid)
        self.build(2 * node + 1, mid+1, right)
        self.st[node] = (
            max(self.st[node*2][0], self.st[node*2+1][0]),
            min(self.st[node*2][1], self.st[node*2+1][1]),
        )

    def query(self, query_left, query_right, node=1, left=0, right=None):
        if right == None: right = self.n-1
        if query_left > right or query_right < left:
            return (-math.inf, math.inf)
        if query_left <= left and query_right >= right:
            return self.st[node]

        mid = left + (right - left) // 2
        lmx, lmn = self.query(query_left, query_right, node*2, left, mid)
        rmx, rmn = self.query(query_left, query_right, node*2+1, mid+1, right)
        return(
            max(lmx, rmx),
            min(lmn, rmn)
        )


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SegmentTree(nums)
        mh = []
        mx, mn = st.query(0, n - 1)
        heapq.heappush(mh, (-(mx - mn), 0, n-1))
        seen = set()
        seen.add((0, n-1))
        res = 0
        while k:
            k -= 1
            v, l, r = heapq.heappop(mh)
            v *= -1
            res += v

            if l + 1 <= r and not (l+1, r) in seen:
                mx, mn = st.query(l+1, r)
                heapq.heappush(mh, (-(mx - mn), l+1, r))
                seen.add((l+1, r))

            if r - 1 >= l and not (l, r-1) in seen:
                mx, mn = st.query(l, r-1)
                heapq.heappush(mh, (-(mx - mn), l, r-1))
                seen.add((l, r-1))

        return res