"""
LeetCode :: October 2021 Challenge :: 75. Sort Colors
jramaswami
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pass, constant space.
        freqs = [0, 0, 0]

        for n in nums:
            freqs[n] += 1

        for i in range(0, freqs[0]):
            nums[i] = 0
        for i in range(freqs[0], freqs[0] + freqs[1]):
            nums[i] = 1
        for i in range(freqs[0] + freqs[1], len(nums)):
            nums[i] = 2
