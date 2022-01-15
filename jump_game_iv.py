"""
LeetCode :: January 2022 Challenge :: 1345. Jump Game IV
jramaswami
"""


import collections
import math


class Solution:
    def minJumps(self, arr):

        long_jumps = collections.defaultdict(list)
        for off, n in enumerate(reversed(arr)):
            i = len(arr) - off - 1
            long_jumps[n].append(i)

        dist = [math.inf for _ in arr]
        queue = collections.deque()
        queue.append(0)
        dist[0] = 0
        while queue:
            u = queue.popleft()
            d = dist[u]

            if u == len(arr) - 1:
                return d

            # Move forward one.
            if u + 1 < len(arr) and d + 1 < dist[u+1]:
                if u + 1 == len(arr) - 1:
                    return d + 1
                queue.append(u+1)
                dist[u+1] = d + 1

            # Move backward one.
            if u - 1 >= 0 and d + 1 < dist[u-1]:
                queue.append(u-1)
                dist[u-1] = d + 1

            # Jump to index with same value.
            for v in long_jumps[arr[u]]:
                if u != v and d + 1 < dist[v]:
                    if v == len(arr) - 1:
                        return d + 1
                    queue.append(v)
                    dist[v] = d + 1


def test_1():
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    expected = 3
    assert Solution().minJumps(arr) == expected


def test_2():
    arr = [7]
    expected = 0
    assert Solution().minJumps(arr) == expected


def test_3():
    arr = [7,6,9,6,9,6,9,7]
    expected = 1
    assert Solution().minJumps(arr) == expected


def test_4():
    "TLE"
    arr = [7] * (pow(10,5) - 1)
    arr.append(11)
    expected = 2
    assert Solution().minJumps(arr) == expected
