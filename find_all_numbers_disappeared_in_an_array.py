"""
binarysearch.com :: Find All Numbers Disappeared in Array
jramaswami
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        # Find the length of the array
        N = len(nums)
        # Set up a boolean array to indicate that n is in nums.
        present = [0 for _ in range(N+1)]
        present[0] = 1  # ignore zero
        # Iterate over nums and mark every num in nums as present.  Duplicates
        # will not cause a problem.
        for n in nums:
            present[n] = 1

        return [i for i, p in enumerate(present) if p == 0]


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
