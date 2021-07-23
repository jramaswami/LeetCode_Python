"""
LeetCode :: Array Module :: Squares of a Sorted Array
jramaswami
"""

from collections import deque


class Solution:
    def sortedSquares(self, nums):
        squares = deque(n * n for n in nums)
        # The negative numbers at the left of nums have become positive
        # numbers.  Just take the max from the left or right and append it to
        # the solution.  This could be done with two pointers, but a deque is
        # easier for coding.
        soln = []
        while squares:
            if squares[0] > squares[-1]:
                soln.append(squares.popleft())
            else:
                soln.append(squares.pop())
        return soln[::-1]


def test_1():
    nums = [-4,-1,0,3,10]
    expected = [0,1,9,16,100]
    assert Solution().sortedSquares(nums) == expected


def test_2():
    nums = [-7,-3,2,3,11]
    expected = [4,9,9,49,121]
    assert Solution().sortedSquares(nums) == expected
