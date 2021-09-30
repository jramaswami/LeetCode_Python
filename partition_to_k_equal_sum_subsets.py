"""
LeetCode :: September 2021 Challenge :: Partition to K Equal Sum Subsets
jramaswami
"""


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


        def solve(index, acc, target):
            """Recursive solution."""
            # Base case
            if index >= len(nums):
                return (a == target for a in acc)

            for i, _ in enumerate(acc):
                if acc[i] + nums[index] <= target:
                    acc[i] += nums[index]
                    if solve(index + 1, acc, target):
                        return True
                    acc[i] -= nums[index]
            return False

        return solve(0, [0 for _ in range(k)], sum(nums) // k)


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
