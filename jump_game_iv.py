"""
LeetCode :: January 2022 Challenge :: 1345. Jump Game IV
jramaswami
"""


import collections
import math


class Solution:
    def minJumps(self, arr):

        dist = [math.inf for _ in arr]
        long_jumps = collections.defaultdict(list)
        for i, n in enumerate(arr):
            long_jumps[n].append(i)

        queue = set()
        new_queue = set()
        dist[0] = 0
        queue.add(0)
        while queue:
            for u in queue:
                # Move back one.
                if u + 1 < len(arr) and dist[u] + 1 < dist[u+1]:
                    dist[u+1] = dist[u] + 1
                    new_queue.add(u+1)
                # Move forward one.
                if u - 1 >= 0 and dist[u] + 1 < dist[u-1]:
                    dist[u-1] = dist[u] + 1
                    new_queue.add(u-1)

                # Jump to index with same value.
                for v in long_jumps[arr[u]]:
                    if u != v and dist[u] + 1 < dist[v]:
                        dist[v] = dist[u] + 1
                        new_queue.add(v)
            queue, new_queue = new_queue, set()
        return dist[-1]



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
    expected = 1
    assert Solution().minJumps(arr) == expected
