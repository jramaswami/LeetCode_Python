"""
LeetCode :: August 2021 Challenge :: Subsets II
jramaswami
"""

import collections


def powerset(keys, freqs, key_index, acc):
    """
    Generator for powerset. Yields a tuple that contains the frequency of
    each key in the subset.
    """
    if key_index >= len(keys):
        yield tuple(acc)
    else:
        key = keys[key_index]
        max_freq = freqs[key]
        for m in range(max_freq + 1):
            acc[key_index] = m
            yield from powerset(keys, freqs, key_index + 1, acc)


def build_subset(subset_map, keys):
    """Function that takes the set map & keys to produce the subset."""
    acc = []
    for n, k in zip(subset_map, keys):
        acc.extend(k for _ in range(n))
    return acc


class Solution:
    def subsetsWithDup(self, nums):
        freqs = collections.Counter(nums)
        keys = list(freqs.keys())
        acc = [0 for _ in keys]
        return list(build_subset(m, keys) for m in powerset(keys, freqs, 0, acc))


def test_1():
    nums = [1,2,2]
    expected = [[],[1],[1,2],[1,2,2],[2],[2,2]]
    assert sorted(Solution().subsetsWithDup(nums)) == sorted(expected)
