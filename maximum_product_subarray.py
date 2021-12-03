"""
LeetCode :: December 2021 Challenge :: 152. Maximum Product Subarray
jramaswami
"""


import math


class Solution:
    def maxProduct(self, nums):
        curr = 1
        # Start with a solution that is the maximum for a single number.
        soln = max(nums)
        first_neg = 0
        for n in nums:
            if n == 0:
                # If n is zero, we must start over.  Reset curr to 1.
                # A zero solution is possible, so apply it.
                curr = 1
            else:
                # Apply n to curr.
                curr *= n
                if curr < 1:
                    if first_neg:
                        # If curr is negative and we have already had a
                        # negative product, remove all the numbers up to
                        # and including that first negative number from curr
                        # and apply that as a possible solution.
                        soln = max(soln, curr // first_neg)
                    else:
                        # If we have not had a negative number yet, set the
                        # first_neg.
                        first_neg = curr
                else:
                    # If the product is positive, apply it to the solution.
                    soln = max(soln, curr)
        return soln


def test_1():
    nums = [2,3,-2,4]
    expected = 6
    assert Solution().maxProduct(nums) == expected


def test_2():
    nums = [-2,0,-1]
    expected = 0
    assert Solution().maxProduct(nums) == expected


def test_3():
    nums = [-8, -6, -5, -10, 9, -9, 2, -2, 9, 0, 6, -4, 3, -2, -10, 10]
    expected = 6998400
    assert Solution().maxProduct(nums) == expected


def test_4():
    "WA"
    nums = [-2]
    expected = -2
    assert Solution().maxProduct(nums) == expected


def test_5():
    "WA"
    nums = [1,0,-1,2,3,-5,-2]
    expected = 60
    assert Solution().maxProduct(nums) == expected


def test_6():
    "WA"
    nums = [-1,0,-2,2]
    expected = 2
    assert Solution().maxProduct(nums) == expected
