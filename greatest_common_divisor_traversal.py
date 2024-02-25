"""
LeetCode
2709. Greatest Common Divisor Traversal
February 2024 Challenge
jramaswami
"""


from typing import List


def sieve_primes(limit):
    is_prime = [True for _ in range(limit)]
    is_prime[0] = is_prime[1] = False
    for x in range(4, limit, 2):
        is_prime[x] = False
    for p in range(3, limit, 2):
        if is_prime[p]:
            for x in range(p+p, limit, p):
                is_prime[x] = False
    return [p for p in range(limit) if is_prime[p]]


class UnionFind:

    def __init__(self, N):
        self.id = list(range(N))
        self.size = [1 for _ in self.id]

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b, = b, a
            self.size[a] += self.size[b]
            self.id[b] = a

    def are_united(self, a, b):
        return self.find(a) == self.find(b)


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if any(n == 1 for n in nums):
            return False

        # nums[i] <= 10^5
        # prime factors <= sqrt(10^5) ~ 317
        primes = sieve_primes(350)
        uf = UnionFind(pow(10,5)+1)
        for i, n in enumerate(nums):
            x = n
            for p in primes:
                if p > x:
                    break
                if x % p == 0:
                    uf.union(p, n)
                while x % p == 0:
                    x //= p
            if x > 1:
                uf.union(x, n)

        x = uf.find(nums[0])
        return all(uf.find(n) == x for n in nums)


def test_1():
    nums = [2,3,6]
    expected = True
    assert Solution().canTraverseAllPairs(nums) == expected


def test_2():
    nums = [3,9,5]
    expected = False
    assert Solution().canTraverseAllPairs(nums) == expected


def test_3():
    nums = [4,3,12,8]
    expected = True
    assert Solution().canTraverseAllPairs(nums) == expected


def test_4():
    nums = [1,1,1]
    expected = False
    assert Solution().canTraverseAllPairs(nums) == expected


def test_5():
    "WA"
    nums = [920,429,616,42,385,780,728,795,630,112,420,462,210,143,78,792,770,794,462,910,286,990,390,616,385,275,546,990,924,567,715,156,429,385,660,660,693,28,770,945,399,840,440,231,210,780,210,910,60,546,210,840,308,715,858,704,260,770,735,975,910,715,286,420,770,650,462,845,390,990,312,176,715,624,110,750,990,528,546,819,390,770,10,390,770,461,520,539,770,490,910,364,91,468,462,260,770,525,858,195,378,840,429,210,308,819,840,336,770,182,840,130,165,420,546,462,390,924,468,735,286,630,264,819,308,720,770,198,420,924,364,780,429,825,858,770,198,870,990,465,660,294,546]
    expected = False
    assert Solution().canTraverseAllPairs(nums) == expected


def test_6():
    "WA"
    nums = [1]
    expected = True
    assert Solution().canTraverseAllPairs(nums) == expected