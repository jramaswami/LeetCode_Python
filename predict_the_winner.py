"""
LeetCode
486. Predict the Winner
July 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        MAXIMIZER, MINIMIZER = True, False
        def rec(left, right, player):
            if left > right:
                return 0

            if player == MAXIMIZER:
                return max(
                    nums[left] + rec(left+1, right, not MAXIMIZER),
                    nums[right] + rec(left, right-1, not MAXIMIZER)
                )

            return min(
                rec(left+1, right, not MINIMIZER) - nums[left],
                rec(left, right-1, not MINIMIZER) - nums[right]
            )

        score = rec(0, len(nums) - 1, MAXIMIZER)
        return score >= 0


def test_1():
    nums = [1,5,2]
    expected = False
    assert Solution().PredictTheWinner(nums) == expected


def test_2():
    nums = [1,5,233,7]
    expected = True
    assert Solution().PredictTheWinner(nums) == expected