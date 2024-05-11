"""
LeetCode
857. Minimum Cost to Hire K Workers
May 2024 Challenge
jramaswami

Thank You NeetCode!
"""


import collections
import heapq
import math
from typing import List


Worker = collections.namedtuple('Worker', ['ratio', 'wage', 'quality'])


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = [Worker(w / q, w, q) for q, w in zip(quality, wage)]
        workers.sort()

        soln = math.inf
        queue = []
        quality_sum = 0
        for w in workers:
            heapq.heappush(queue, (-w.quality, -w.wage, w))
            quality_sum += w.quality
            while len(queue) > k:
                _, _, t = heapq.heappop(queue)
                quality_sum -= t.quality

            if len(queue) == k:
                soln = min(soln, w.ratio * quality_sum)
        return soln


EPS = pow(10, -5)


def test_1():
    quality = [10,20,5]
    wage = [70,50,30]
    k = 2
    expected = 105.00000
    result = Solution().mincostToHireWorkers(quality, wage, k)
    assert abs(result - expected) < EPS



def test_2():
    quality = [3,1,10,10,1]
    wage = [4,8,2,2,7]
    k = 3
    expected = 30.66667
    result = Solution().mincostToHireWorkers(quality, wage, k)
    assert abs(result - expected) < EPS