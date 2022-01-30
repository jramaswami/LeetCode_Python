"""
LeetCode :: January 2022 Challenge :: 189. Rotate Array
jramaswami
"""


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        # First gather the numbers that will rotate around.
        last = list(nums[-k:])
        # Then loop over numbers from start by k and rotate them
        # forward.
        for start in range(k):
            t = nums[start]
            for r in  range(start + k, len(nums), k):
                t, nums[r] = nums[r], t
        # Rotate the last numbers around to the front.
        nums[:k] = last


def test_1():
    nums = [1,2,3,4,5,6,7]
    k = 3
    expected = [5,6,7,1,2,3,4]
    Solution().rotate(nums, k)
    assert nums == expected


def test_2():
    nums = [-1,-100,3,99]
    k = 2
    expected = [3,99,-1,-100]
    Solution().rotate(nums, k)
    assert nums == expected


def test_3():
    "WA"
    nums = [1]
    k = 0
    expected = [1]
    Solution().rotate(nums, k)
    assert nums == expected


def test_4():
    "RTE"
    nums = [-1]
    k = 2
    expected = [-1]
    Solution().rotate(nums, k)
    assert nums == expected
