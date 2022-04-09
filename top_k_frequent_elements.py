"""
LeetCode :: April 2022 Challenge :: 347. Top K Frequent Elements
jramaswami
"""


import collections


class Solution:

    def topKFrequent(self, nums, k):
        ctr = collections.Counter(nums)
        freqs = [[] for _ in range(len(nums)+1)]
        for val, freq in ctr.items():
            freqs[freq].append(val)

        soln = []
        i = len(nums)
        while len(soln) < k:
            soln.extend(freqs[i])
            i -= 1
        return soln


def test_1():
    nums = [1,1,1,2,2,3]
    k = 2
    expected = [1,2]
    result = Solution().topKFrequent(nums, k)
    assert sorted(result) == sorted(expected)


def test_2():
    nums = [1]
    k = 1
    expected = [1]
    result = Solution().topKFrequent(nums, k)
    assert sorted(result) == sorted(expected)
