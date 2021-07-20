"""
LeetCode :: July 2021 Challenge :: Shuffle An Array
jramaswami

Randomly shuffle an array such that all permutations of the array should be
equally likely as a result of the shuffling.  The Fisher-Yates shuffle does
exactly this.
"""


import secrets


class Solution:

    def __init__(self, nums):
        # Do not mutate original list. Keep the copy.
        self.nums = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return list(self.nums)

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        shuffled = list(self.nums)
        # Fisher-Yates shuffle
        for i in range(len(self.nums) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
