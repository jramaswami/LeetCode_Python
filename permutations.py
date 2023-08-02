"""
LeetCode
46. Permutations
August 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        soln = []

        def rec(bitset, acc):
            # Base Case
            if bitset == (1 << len(nums)) - 1:
                soln.append(list(acc))
                return

            for i, k in enumerate(nums):
                if (bitset & (1 << i)) == 0:
                    acc.append(k)
                    rec(bitset | (1 << i), acc)
                    acc.pop()

        rec(0, [])
        return soln


def test_1():
    nums = [1,2,3]
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    result = Solution().permute(nums)
    assert sorted(result) == sorted(expected)


def test_2():
    nums = [0,1]
    expected = [[0,1], [1,0]]
    result = Solution().permute(nums)
    assert sorted(result) == sorted(expected)