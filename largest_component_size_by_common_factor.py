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
    def __init__(self):
        limit = pow(10,5) // 2
        is_prime = [True for _ in range(limit + 1)]
        is_prime[0] = is_prime[1] = False
        for i in range(4, len(is_prime), 2):
            is_prime[i] = False
        p = 3
        while p * p <= len(is_prime):
            if is_prime[p]:
                for i in range(p + p, len(is_prime), p):
                    is_prime[i] = False
            p += 2
        self.PRIMES = [p for p, _ in enumerate(is_prime) if is_prime[p]]

    def largestComponentSize(self, nums):
        uf = UnionFind()
        for n in nums:
            uf.make_set(n)

        for P in self.PRIMES:
            A = [n for n in nums if n % P == 0]
            for k in A[1:]:
                uf.union_set(A[0], k)
        return uf.max_size()


def test_1():
    nums = [20,50,9,63]
    expected = 2
    assert Solution().largestComponentSize(nums) == expected


def test_2():
    nums = [2,3,6,7,4,12,21,39]
    expected = 8
    assert Solution().largestComponentSize(nums) == expected


def test_3():
    nums = list(range(1, pow(10, 4)))
    expected = 9438
    assert Solution().largestComponentSize(nums) == expected