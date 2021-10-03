"""
LeetCode :: October 2021 Challenge :: Jump Game
jramaswami
"""


class Solution:

    def canJump(solve, nums):
        dp = [False for _ in nums]
        dp[0] = True
        for i, n in enumerate(nums):
            if dp[i]:
                for j in range(1, n+1):
                    if i+j < len(nums):
                        dp[i+j] = True
        return dp[-1]


def test_1():
    nums = [2,3,1,1,4]
    assert Solution().canJump(nums) == True


def test_2():
    nums = [3,2,1,0,4]
    assert Solution().canJump(nums) == False
