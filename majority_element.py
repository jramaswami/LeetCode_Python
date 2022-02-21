"""
LeetCode :: February 2022 Challenge :: 169. Majority Element
jramaswami
"""


class Solution:

    def majorityElement(self, nums):
        # Boyer Moore
        candidate = nums[0]
        count = 1
        for n in nums[1:]:
            if n != candidate:
                count -= 1
            else:
                count += 1
            if count == 0:
                candidate = n
                count = 1

        count = sum(1 if n == candidate else 0 for n in nums)
        assert count > len(nums) // 2
        return candidate


def test_1():
    nums = [3,2,3]
    expected = 3
    assert Solution().majorityElement(nums) == expected


def test_2():
    nums = [2,2,1,1,1,2,2]
    expected = 2
    assert Solution().majorityElement(nums) == expected


def test_3():
    "RTE"
    nums = [3, 3, 4]
    expected = 3
    assert Solution().majorityElement(nums) == expected
