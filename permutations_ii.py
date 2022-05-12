"""
LeetCode :: May 2022 Challenge :: Permutations II
jramaswami
"""


import collections


class Solution:

    def permuteUnique(self, nums):

            freqs = collections.Counter(nums)
            soln = []

            def solve0(i, acc):
                if i >= len(nums):
                    soln.append(list(acc))
                else:
                    for k in freqs:
                        if freqs[k] > 0:
                            freqs[k] -= 1
                            acc.append(k)
                            solve0(i+1, acc)
                            acc.pop()
                            freqs[k] += 1

            solve0(0, [])
            return soln


def test_1():
    nums = [1,1,2]
    expected = [[1,1,2], [1,2,1], [2,1,1]]
    result = Solution().permuteUnique(nums)
    assert sorted(result) == sorted(expected)


def test_2():
    nums = [1,2,3]
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    result = Solution().permuteUnique(nums)
    assert sorted(result) == sorted(expected)