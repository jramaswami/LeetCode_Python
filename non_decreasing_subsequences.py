"""
LeetCode
491. Non-decreasing Subsequences
January 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        soln = set()

        def rec(i, acc):
            if i >= len(nums):
                if len(acc) > 1:
                    print(acc)
                    soln.add(tuple(acc))
            else:
                # Skip this number.
                rec(i+1, acc)

                # Choose this number, if possible.
                if not acc or nums[i] >= acc[-1]:
                    acc.append(nums[i])
                    rec(i+1, acc)
                    acc.pop()

        rec(0, [])
        return [list(t) for t in soln]




def test_1():
    nums = [4,6,7,7]
    expected = [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    assert sorted(Solution().findSubsequences(nums)) == sorted(expected)


def test_2():
    nums = [4,4,3,2,1]
    expected = [[4,4]]
    assert sorted(Solution().findSubsequences(nums)) == sorted(expected)