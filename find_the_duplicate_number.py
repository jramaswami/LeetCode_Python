"""
LeetCode :: March 2022 Challenge :: 287. Find the Duplicate Number
jramaswami

REF: https://www.youtube.com/watch?v=wjYnzkAhcNk
"""


class Solution:
    def findDuplicate(self, nums):
        def succ(i):
            return nums[i]

        slow = fast = 0
        while True:
            slow = succ(slow)
            fast = succ(succ(fast))
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = succ(slow)
            slow2 = succ(slow2)
            if slow == slow2:
                return slow


def test_1():
    nums = [1,3,4,2,2]
    expected = 2
    assert Solution().findDuplicate(nums) == expected


def test_2():
    nums = [3,1,3,4,2]
    expected = 3
    assert Solution().findDuplicate(nums) == expected


def test_3():
    "WA"
    nums = [2,2,2,2,2]
    expected = 2
    assert Solution().findDuplicate(nums) == expected
