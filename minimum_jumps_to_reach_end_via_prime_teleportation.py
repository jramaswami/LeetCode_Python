"""
LeetCode
3629. Minimum Jumps to Reach End via Prime Teleportation
May 2026 Challenge
jramaswami
"""


from typing import List
import heapq


def sieve():
    N = pow(10,6)
    is_prime = [True for _ in range(pow(10,6))]
    is_prime[0] = is_prime[1] = False
    for x in range(4, N, 2):
        is_prime[x] = False

    for p in range(3, pow(10,3)+1, 2):
        if is_prime[p]:
            for x in range(2*p, N, p):
                is_prime[x] = False
    return is_prime


PRIMES = sieve()


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        INF = pow(10, 10)
        soln = [INF for _ in nums]
        soln[0] = 0
        queue = [(0, 0)]
        while queue:
            d, i = heapq.heappop(queue)
            if i == len(nums) - 1:
                return d
            x = nums[i]
            if d == soln[i]:
                # left, right
                if i + 1 < len(nums) and d + 1 < soln[i + 1]:
                    soln[i + 1] = d + 1
                    heapq.heappush(queue, (d+1, i+1))
                if i - 1 >= 0 and d + 1 < soln[i - 1]:
                    soln[i - 1] = d + 1
                    heapq.heappush(queue, (d+1, i-1))
                if PRIMES[x]:
                    for j, y in enumerate(nums):
                        if d + 1 < soln[j] and y % x == 0:
                            soln[j] = d + 1
                            heapq.heappush(queue, (d+1, j))


def test_668():
    nums = [7,5,7]
    assert Solution().minJumps(nums) == 1
