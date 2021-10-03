"""
LeetCode :: October 2021 Challenge :: Jump Game
jramaswami
"""


class Solution:

    def canJump(solve, nums):
        max_reachable = 0
        for i, n in enumerate(nums):
            if i <= max_reachable:
                max_reachable =  max(max_reachable, i + n)
        return max_reachable >= len(nums) - 1


def test_1():
    nums = [2,3,1,1,4]
    assert Solution().canJump(nums) == True


def test_2():
    nums = [3,2,1,0,4]
    assert Solution().canJump(nums) == False


def test_3():
    nums = [1,1,2,0,0,0,1]
    assert Solution().canJump(nums) == False


def test_4():
    """WA"""
    nums = [0]
    assert Solution().canJump(nums) == True
