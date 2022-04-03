"""
LeetCode :: April 2022 Challenge :: 31. Next Permutation
jramaswami
"""


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pandita's Algorithm.
        # 1. Find the largest index k such that a[k] < a[k + 1]. If no such
        # index exists, the permutation is the last permutation.
        k = -1
        for i, _ in enumerate(nums[:-1]):
            if nums[i] < nums[i+1]:
                k = i

        if k < 0:
            nums.sort()
            return

        # 2. Find the largest index l greater than k such that a[k] < a[l].
        l = -1
        for i, _ in enumerate(nums[k+1:], start=k+1):
            if nums[k] < nums[i]:
                l = i

        # 3. Swap the value of a[k] with that of a[l].
        nums[k], nums[l] = nums[l], nums[k]

        # 4. Reverse the sequence from a[k + 1] up to and including the final
        # element a[n].
        nums[k+1:] = nums[k+1:][::-1]


def test_1():
    nums = [1,2,3]
    expected = [1,3,2]
    Solution().nextPermutation(nums)
    assert nums == expected


def test_2():
    nums = [3,2,1]
    expected = [1,2,3]
    Solution().nextPermutation(nums)
    assert nums == expected


def test_3():
    nums = [1,1,5]
    expected = [1,5,1]
    Solution().nextPermutation(nums)
    assert nums == expected


def test_4():
    nums = []
    expected = []
    Solution().nextPermutation(nums)
    assert nums == expected


def test_5():
    nums = [5]
    expected = [5]
    Solution().nextPermutation(nums)
    assert nums == expected
