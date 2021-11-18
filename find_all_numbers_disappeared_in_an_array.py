"""
LeetCode :: November 2021 Challenge :: 448. Find All Numbers Disappeared in an Array
jramaswami
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        # Mark n as present by changing nums[n] to a negative number.
        # (Adjust for zero based indexing.)
        for n in nums:
            i = abs(n) - 1
            # Only mark if it hasn't already been marked.
            if nums[i] >= 0:
                nums[i] *= -1
        # Gather indices where n is a positive number and therefore not
        # present.  (Adjust for zero based indexing.)
        return [i+1 for i, n in enumerate(nums) if n > 0]


def test_1():
    nums = [4,3,2,7,8,2,3,1]
    expected = [5,6]
    assert Solution().findDisappearedNumbers(nums) == expected


def test_2():
    nums = [1, 1]
    expected = [2]
    assert Solution().findDisappearedNumbers(nums) == expected


def test_3():
    nums = [1, 2, 3, 4, 5]
    expected = []
    assert Solution().findDisappearedNumbers(nums) == expected


def test_4():
    nums = [1, 1, 1, 1, 1]
    expected = [2, 3, 4, 5]
    assert Solution().findDisappearedNumbers(nums) == expected
