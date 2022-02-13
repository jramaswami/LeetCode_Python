"""
LeetCode :: February 2022 Challenge :: 78. Subsets
jramaswami
"""


class Solution:

    def subsets(self, nums):

        def solve(index, nums, acc, soln):
            if index >= len(nums):
                soln.append(list(acc))
                return

            solve(index + 1, nums, acc, soln)
            acc.append(nums[index])
            solve(index + 1, nums, acc, soln)
            acc.pop()

        soln = []
        acc = []
        solve(0, nums, acc, soln)
        return soln


def test_1():
    nums = [1,2,3]
    expected = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    result = Solution().subsets(nums)
    assert sorted(result) == sorted(expected)


def test_2():
    nums = [0]
    expected = [[],[0]]
    result = Solution().subsets(nums)
    assert sorted(result) == sorted(expected)


