"""
LeetCode :: August 2022 Challenge :: 659. Split Array into Consecutive Subsequences
jramaswami
"""


from typing import *
import math

class Solution:

    def isPossible(self, nums: List[int]) -> bool:
        H = [[nums[0]]]
        for n in nums[1:]:
            # Find the smallest sequence that requires me.
            sm_length = math.inf
            sm_list = None
            H0 = []
            for h in H:
                if h[-1] == n - 1 and len(h) < sm_length:
                    sm_length = len(h)
                    sm_list = h
            if sm_list:
                # If we found one then add n to that list.
                sm_list.append(n)
            else:
                # If we did not find one then we must add another list.
                H.append([n])

        return all(len(h) >= 3 for h in H)


def test_1():
    nums = [1,2,3,3,4,5]
    expected = True
    assert Solution().isPossible(nums) == expected


def test_2():
    nums = [1,2,3,3,4,4,5,5]
    expected = True
    assert Solution().isPossible(nums) == expected


def test_3():
    nums = [1,2,3,4,4,5]
    expected = False
    assert Solution().isPossible(nums) == expected