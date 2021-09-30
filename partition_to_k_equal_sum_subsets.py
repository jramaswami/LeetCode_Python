"""
LeetCode :: September 2021 Challenge :: Partition to K Equal Sum Subsets
jramaswami
"""


from collections import defaultdict
from itertools import combinations
from functools import reduce
from operator import and_


class Solution:

    def canPartitionKSubsets(self, nums, k):
        def powerset_generator(nums):
            """Use bitmasks to generate powerset of nums."""
            N = len(nums)
            for mask in range(1 << N):
                yield mask, sum(n for i, n in enumerate(nums) if mask & (1 << i))

        def disjoint(combo):
            """Return True if the bitmasks in combo do not intersect."""
            bits = combo[0]
            for c in combo[1:]:
                if bits & c:
                    return False
                bits |= c
            return True

        # Take the powerset of nums and get each possible set and its sum.
        sums = defaultdict(list)
        for mask, p in powerset_generator(nums):
            sums[p].append(mask)

        # Look at every k-combination of sums and return True if one of the
        # combination has not intersections.
        for s in sums:
            for combo in combinations(sums[s], k):
                if disjoint(combo):
                    print(nums)
                    for c in combo:
                        print(f"{c:016b}", to_tuple(nums, c), s, sum(to_tuple(nums, c)))
                    return True
        return False



def to_tuple(nums, mask):
    return tuple(n for i, n in enumerate(nums) if mask & (1 << i))

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
