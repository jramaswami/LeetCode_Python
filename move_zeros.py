"""
LeetCode :: Array Module :: Move Zeros
jramaswami
"""


class Solution:
    def moveZeroes(self, nums):
        # Done in place as suggested by the module instructions.
        zeros = 0
        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
            else:
                nums[i - zeros] = n

        for i in range(len(nums) - zeros, len(nums)):
            nums[i] = 0
        return nums



def test_1():
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    assert Solution().moveZeroes(nums) == expected


def test_2():
    nums = [0]
    expected = [0]
    assert Solution().moveZeroes(nums) == expected
