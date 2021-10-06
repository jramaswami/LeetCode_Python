"""
LeetCode :: October 2021 Challenge :: 442. Find All Duplicates in an Array
jramaswami
"""


class Solution:

    def findDuplicates(self, nums):
        soln = []
        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                soln.append(abs(n))
            else:
                nums[i] *= -1
        return soln


def test_1():
    nums = [4,3,2,7,8,2,3,1]
    expected = [2, 3]
    assert sorted(Solution().findDuplicates(nums)) == sorted(expected)


def test_2():
    nums = [1, 1, 2]
    expected = [1]
    assert sorted(Solution().findDuplicates(nums)) == sorted(expected)


def test_3():
    nums = [1]
    expected = []
    assert sorted(Solution().findDuplicates(nums)) == sorted(expected)
