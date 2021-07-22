"""
LeetCode :: July 2021 Challenge :: Partition Array Into Disjoint Intervals
jramaswami
"""


from math import inf


class Solution:
    def partitionDisjoint(self, nums):
        # Get an array of the min from i to the end of the array.
        suffix_min = [inf for _ in nums]
        curr_min = inf
        for i in range(len(nums)-1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suffix_min[i] = curr_min
        suffix_min.append(inf)

        # Iterate over array.  If the curr max from 0 to j is <= the curr min
        # from j+1 to the end then you can left partition at j.
        curr_max = -inf
        for j, n in enumerate(nums):
            curr_max = max(curr_max, n)
            if curr_max <= suffix_min[j+1]:
                return j + 1


def test_1():
    nums = [5,0,3,8,6]
    expected = 3
    assert Solution().partitionDisjoint(nums) == expected


def test_2():
    nums = [1,1,1,0,6,12]
    expected = 4
    assert Solution().partitionDisjoint(nums) == expected


def test_3():
    nums = [1, 2, 3, 4, 5, 6]
    expected = 1
    assert Solution().partitionDisjoint(nums) == expected


def test_4():
    nums = [5, 4, 3, 2, 1]
    expected = 5
    assert Solution().partitionDisjoint(nums) == expected
