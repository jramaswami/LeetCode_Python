"""
LeetCode :: August 2021 Challenge :: Subsets II
jramaswami
"""

class Solution:
    def subsetsWithDup(self, nums):
        # To get same sets as test cases.
        nums.sort()

        # Use bitmask to get all subsets.
        N = 1 << (len(nums) + 1)
        all_subsets = []
        for n in range(N):
            subset = []
            for b in range(len(nums)):
                if n & (1 << b):
                    subset.append(nums[b])
            all_subsets.append(subset)

        # Dedupe the subsets using sorting to find duplicates.
        all_subsets.sort()
        unique_subsets = []
        for subset in all_subsets:
            if not unique_subsets or subset != unique_subsets[-1]:
                unique_subsets.append(subset)
        return unique_subsets


def test_1():
    nums = [1,2,2]
    expected = [[],[1],[1,2],[1,2,2],[2],[2,2]]
    assert sorted(Solution().subsetsWithDup(nums)) == sorted(expected)
