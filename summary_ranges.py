"""
LeetCode :: February 2022 Challenge :: 228. Summary Ranges
jramaswami
"""


class Solution:

    def summaryRanges(self, nums):
        # Boundary case: nums is empty
        if not nums:
            return []

        ranges = [[nums[0], nums[0]]]
        for n in nums[1:]:
            if n - 1 == ranges[-1][-1]:
                ranges[-1][-1] = n
            else:
                ranges.append([n, n])

        def fmt(rng):
            if rng[0] == rng[1]:
                return str(rng[0])
            return f"{rng[0]}->{rng[1]}"

        return [fmt(rng) for rng in ranges]


def test_1():
    nums = [0,1,2,4,5,7]
    expected = ["0->2","4->5","7"]
    assert Solution().summaryRanges(nums) == expected


def test_2():
    nums = [0,2,3,4,6,8,9]
    expected = ["0","2->4","6","8->9"]
    assert Solution().summaryRanges(nums) == expected


def test_3():
    "RTE"
    nums = []
    expected = []
    assert Solution().summaryRanges(nums) == expected
