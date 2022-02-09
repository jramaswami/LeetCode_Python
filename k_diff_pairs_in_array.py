"""
LeetCode :: February 2022 Challenge :: 532. K-diff Pairs in an Array
jramaswami
"""


class Solution:

    def findPairs(self, nums, k):
        S = set()
        solns = set()
        for n in nums:
            # n - x = k      n - x = -k
            # n = k + x      n = x - k
            # n - k = x      n + k = x
            if n - k in S:
                solns.add((n - k, n))
            if n + k in S:
                solns.add((n, n + k))
            S.add(n)
        return len(solns)


def test_1():
    nums = [3,1,4,1,5]
    k = 2
    expected =  2
    assert Solution().findPairs(nums, k) == expected


def test_2():
    nums = [1,2,3,4,5]
    k = 1
    expected = 4
    assert Solution().findPairs(nums, k) == expected


def test_3():
    nums = [1,3,1,5,4]
    k = 0
    expected = 1
    assert Solution().findPairs(nums, k) == expected
