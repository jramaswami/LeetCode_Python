"""
LeetCode :: November 2021 Challenge :: 952. Largest Component Size by Common Factor
jramaswami
"""


import math
import collections
import itertools


class UnionFind:

    def __init__(self):
        self.size = collections.defaultdict(int)
        self.parent = collections.defaultdict(int)

    def make_set(self, u):
        self.size[u] = 1
        self.parent[u] = u

    def find_set(self, u):
        if self.parent[u] == u:
            return u
        p = self.find_set(self.parent[u])
        self.parent[u] = p
        return self.parent[u]

    def union_set(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

    def max_size(self):
        return max(self.size.values())


class Solution:
    def largestComponentSize(self, nums):
        uf = UnionFind()
        for n in nums:
            uf.make_set(n)

        for a, b in itertools.combinations(nums, 2):
            if math.gcd(a, b) > 1:
                print(a, b)
                uf.union_set(a, b)

        return uf.max_size()



def test_1():
    nums = [20,50,9,63]
    expected = 2
    assert Solution().largestComponentSize(nums) == expected


def test_2():
    nums = [2,3,6,7,4,12,21,39]
    expected = 8
    assert Solution().largestComponentSize(nums) == expected
