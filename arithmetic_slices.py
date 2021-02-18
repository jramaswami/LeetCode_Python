"""
LeetCode :: Arithmetic Slices
jramaswami
"""
from typing import *


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # This is an O(N) solution.
        soln = 0
        if len(A) > 2:
            # Start with the first two items in the list.
            sequence_length = 2
            # Get the delta between them.
            delta = A[1] - A[0]
            # For every position in the list.
            for end_index, end_value in enumerate(A[2:], start=2):
                if A[end_index] - A[end_index - 1] == delta:
                    # If the difference between this position and previous is
                    # still delta, then increment the length of the current
                    # sequence by one.
                    sequence_length += 1
                    # Then add the number of sequences longer than three items
                    # that end here to the solution.  (That is length - 2).
                    if sequence_length >= 3:
                        soln += (sequence_length - 2)
                else:
                    # If the difference is not the same, then we must start a
                    # new sequence beginning with A[end_index - 1] and
                    # A[end_index].
                    delta = A[end_index] - A[end_index - 1]
                    sequence_length = 2

        return soln



def test_1():
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3

def test_2():
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4, 7, 8, 9, 10]) == 6

def test_3():
    assert Solution().numberOfArithmeticSlices([1, 2, 4, 5, 7, 8, 10, 11]) == 0

def test_4():
    assert Solution().numberOfArithmeticSlices([4, 3, 2, 1]) == 3

def test_5():
    assert Solution().numberOfArithmeticSlices([]) == 0
