"""
LeetCode :: November 2021 Challenge :: 952. Largest Component Size by Common Factor
jramaswami

Hints from Larry.
"""


import collections


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

        # Get the prime factors for all numbers less than or equal to the
        # maximum number in nums.
        prime_factors = [[] for _ in range(max(nums) + 1)]
        prime_factors[0] = [0]
        prime_factors[1] = [1]
        for P, _ in enumerate(prime_factors[2:], start=2):
            uf.make_set(P)
            if not prime_factors[P]:
                # P is prime since it has no factors.
                for k in range(P, len(prime_factors), P):
                    prime_factors[k].append(P)

        # Use each number to unite its prime factors.
        for n in nums:
            for f in prime_factors[n][1:]:
                uf.union_set(f, prime_factors[n][0])

        # Get the parent for each number using its factors (which should all
        # be in the same set and have the same parent).  Then get a count of
        # the frequence for each parent.
        parents = collections.Counter(uf.find_set(prime_factors[n][0]) for n in nums)
        return max(parents.values())


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