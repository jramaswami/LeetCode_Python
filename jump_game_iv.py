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

        long_jumps_made = set()
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
                if arr[u] not in long_jumps_made:
                    long_jumps_made.add(arr[u])
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
    expected = 2
    assert Solution().minJumps(arr) == expected


def test_5():
    "WA"
    arr = [6, 1, 9]
    expected = 2
    assert Solution().minJumps(arr) == expected


def test_6():
    "WA"
    arr = [51,64,-15,58,98,31,48,72,78,-63,92,-5,64,-64,51,-48,64,48,-76,-86,-5,-64,-86,-47,92,-41,58,72,31,78,-15,-76,72,-5,-97,98,78,-97,-41,-47,-86,-97,78,-97,58,-41,72,-41,72,-25,-76,51,-86,-65,78,-63,72,-15,48,-15,-63,-65,31,-41,95,51,-47,51,-41,-76,58,-81,-41,88,58,-81,88,88,-47,-48,72,-25,-86,-41,-86,-64,-15,-63]
    expected = 4
    assert Solution().minJumps(arr) == expected
