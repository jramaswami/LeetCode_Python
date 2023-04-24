"""
LeetCode
1046. Last Stone Weight
April 2023 Challenge
jramaswami
"""


import heapq


class Solution:

    def lastStoneWeight(self, stones):
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            z = y - x
            if z:
                heapq.heappush(heap, -z)
        if heap:
            return -heapq.heappop(heap)
        return 0


def test_1():
    stones = [2,7,4,1,8,1]
    expected = 1
    assert Solution().lastStoneWeight(stones) == expected


def test_2():
    stones = [1]
    expected = 1
    assert Solution().lastStoneWeight(stones) == expected
