"""
LeetCode :: August 2022 Challenge :: Reduce Array Size to The Half
jramaswami
"""


import collections


class Solution:
    def minSetSize(self, arr):
        if not arr:
            return 0

        freqs = collections.Counter(arr)
        target = len(arr) // 2
        curr = 0
        for i, k, in enumerate(sorted(freqs.values(), reverse=True)):
            curr += k
            print(i, k, curr, target)
            if curr >= target:
                return i + 1
        return -1


def test_1():
    arr = [3,3,3,3,5,5,5,2,2,7]
    expected = 2
    assert Solution().minSetSize(arr) == expected


def test_2():
    arr = [7,7,7,7,7,7]
    expected = 1
    assert Solution().minSetSize(arr) == expected


def test_3():
    arr = [1,9]
    expected = 1
    assert Solution().minSetSize(arr) == expected



def test_4():
    arr = [1000,1000,3,7]
    expected = 1
    assert Solution().minSetSize(arr) == expected


def test_5():
    arr = [1,2,3,4,5,6,7,8,9,10]
    expected = 5
    assert Solution().minSetSize(arr) == expected


def test_6():
    arr = []
    expected = 0
    assert Solution().minSetSize(arr) == expected