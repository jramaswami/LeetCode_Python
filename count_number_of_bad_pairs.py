"""
LeetCode
2364. Count Number of Bad Pairs
February 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Good pair is:
        # j - i == nums[j] - nums[i]
        # j == nums[j] + i - nums[i]
        # j - nums[j] == i - nums[i]
        # For any nums[j] there must exist an i - nums[i] for nums[j] to be good
        soln = 0
        prev_i_minus_nums_i = collections.defaultdict(int)
        for j, nums_j in enumerate(nums):
            j_minus_nums_j = j - nums_j
            # nums[j] is part of j pairs
            # How many good pairs are there?
            good_pairs = prev_i_minus_nums_i[j_minus_nums_j]
            # How many bad pairs are there?
            bad_pairs = j - good_pairs
            # Add the badd pairs to the soln
            soln += bad_pairs
            # Remember the current j_minus_nums_j as i_minus_nums_i since it 
            # has already occurred for any nums after current num
            prev_i_minus_nums_i[j_minus_nums_j] += 1
        return soln
