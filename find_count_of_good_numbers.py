"""
LeetCode
3272. Find the Count of Good Integers
April 2025 Challenge
jramaswami
"""


import collections
import itertools
import math


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        def divisible(digits, divisor):
            multiplier = 1
            number = 0
            for d in reversed(digits):
                number += (multiplier *d)
                multiplier *= 10
            return number % divisor == 0

        # Compute the possible palindromic numbers
        possibles = []
        def rec(i, t, acc):
            if i >= t:
                if n % 2 == 1:
                    possibles.append(tuple(itertools.chain(acc, reversed(acc))))
                else:
                    possibles.append(tuple(itertools.chain(acc, reversed(acc[:-1]))))
                return

            min_number = 0 if i > 0 else 1
            for x in range(min_number, 10):
                acc.append(x)
                rec(i+1, t, acc)
                acc.pop()

        t = n // 2 if n % 2 == 0 else 1 + (n // 2)
        rec(0, t, [])

        soln = 0
        # Which possibles are divisible by k?
        visited_keys = set()
        for candidate in possibles:
            if divisible(candidate, k):
                # How many permutations with replacement are there?
                perms = math.factorial(len(candidate))
                freqs = collections.Counter(candidate)
                key = tuple((f, freqs[f]) for f in sorted(freqs))
                if key not in visited_keys:
                    visited_keys.add(key)
                    for r in freqs.values():
                        perms //= math.factorial(r)
                    # Subtract the number of any that begin with zeros
                    lz_perms = 0
                    if freqs[0]:
                        freqs[0] -= 1
                        lz_perms = math.factorial(len(candidate) - 1)
                        for r in freqs.values():
                            lz_perms //= math.factorial(r)
                        perms -= lz_perms
                    print(candidate, perms, lz_perms)
                    soln += perms

        return soln


def test_1():
    n = 4
    k = 5
    expected = 27
    assert Solution().countGoodIntegers(n, k) == expected


def test_2():
    n = 1
    k = 4
    expected = 2
    assert Solution().countGoodIntegers(n, k) == expected


def test_3():
    n = 5
    k = 6
    expected = 2468
    assert Solution().countGoodIntegers(n, k) == expected