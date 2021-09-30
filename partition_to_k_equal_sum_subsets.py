"""
LeetCode :: September 2021 Challenge :: Partition to K Equal Sum Subsets
jramaswami

Thank You Larry!
"""


from functools import lru_cache


class Solution:

    def canPartitionKSubsets(self, nums, k):
        # Corner case: if k is 1 the answer is always true.
        if k == 1:
            return True

        # Corner case: to divide nums into k parts there must be at least
        # k elements in nums.
        if len(nums) < k:
            return False

        # We are dividing nums into k equal parts, that is all parts
        # have the same sum, call it s.  The total of the array must
        # be k * s, so the sum of the array must be divisible by k.
        if sum(nums) % k:
            return False

        target = sum(nums) // k

        # Use a bitmask to find all possible subsets that add to target.
        possible_subsets = []
        for mask in range(1 << len(nums)):
            subset_sum = sum(n for i, n in enumerate(nums) if mask & (1 << i))
            if subset_sum == target:
                possible_subsets.append(mask)

        @lru_cache(maxsize=None)
        def solve(mask):
            # If we have used all the numbers then return True
            if mask == 0:
                return True

            for pmask in possible_subsets:
                if (mask & pmask) == pmask:
                    # If all the values in pmask are avaiable, recurse after
                    # removing the pmask values from availability.
                    if solve(mask ^ pmask):
                        return True

            return False

        return solve((1 << len(nums)) - 1)


def test_1():
    nums = [4,3,2,3,5,2,1]
    k = 4
    expected = True
    assert Solution().canPartitionKSubsets(nums, k) == expected


def test_2():
    nums = [1,2,3,4]
    k = 3
    expected = False
    assert Solution().canPartitionKSubsets(nums, k) == expected


def test_3():
    nums = [4535, 1759, 3903, 1939, 9637, 9822, 254, 5237, 8474, 9188, 5095, 3277, 1191, 5012, 7605, 8457]
    k = 4
    expected = False
    assert Solution().canPartitionKSubsets(nums, k) == expected


def test_4():
    nums = [4535, 1759, 3903, 1939, 9637, 9822, 254, 5237, 8474, 9188, 5095, 3277, 1191, 5012, 7605, 8457]
    k = 2
    expected = False
    assert Solution().canPartitionKSubsets(nums, k) == expected


def test_5():
    """TLE"""
    nums = [98,102,9,36,57,44,30,35,28,9851,90,29,9751,44,66,9652]
    k = 8
    expected = False
    assert Solution().canPartitionKSubsets(nums, k) == expected


def test_6():
    """TLE"""
    nums = [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908]
    k = 4
    expected = True
    assert Solution().canPartitionKSubsets(nums, k) == expected


def test_7():
    """WA"""
    nums = [2,2,2,2,3,4,5]
    k = 4
    expected = False
    assert Solution().canPartitionKSubsets(nums, k) == expected
