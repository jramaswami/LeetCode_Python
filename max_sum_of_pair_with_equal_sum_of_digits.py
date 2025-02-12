"""
LeetCode
2342. Max Sum of a Pair With Equal Sum of Digits
February 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        visited = collections.defaultdict(int)
        soln = -1
        for n in nums:
            x = sum(int(d) for d in str(n))
            if x in visited:
                soln = max(soln, visited[x] + n)
            visited[x] = max(visited[x], n)
        return soln     
