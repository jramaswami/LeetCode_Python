"""
LeetCode
3655. XOR After Range Multiplication Queries II
April 2026 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=wE2oKAthus4
"""


import collections
import math
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        n = len(nums)
        sq = int(math.sqrt(n))
        mp = collections.defaultdict(list)
        for l, r, k, v in queries:
            if k > sq:
                for i in range(l, r+1, k):
                    nums[i] = nums[i] * v
                    nums[i] %= MOD
            else:
                mp[k].append((l, r, v))

        for k in mp:
            dif = [1] * (n+k)
            for l, r, v in mp[k]:
                dif[l] = dif[l] * v
                dif[l] %= MOD
                rplus1 = l + ((r - l) // k + 1) * k
                dif[rplus1] = dif[rplus1] * pow(v, -1, MOD)
                dif[rplus1] %= MOD

            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k]
                dif[i] %= MOD

            for i in range(n):
                nums[i] = dif[i] * nums[i]
                nums[i] %= MOD

        res = 0
        for x in nums:
            res ^= x
        return res