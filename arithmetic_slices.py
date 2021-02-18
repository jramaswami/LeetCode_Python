"""
LeetCode :: Arithmetic Slices
jramaswami
"""
from typing import *


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        soln = 0
        # Start point of sequence can must be such that there are 2 remaining
        # elements in the array.
        for start_index, start_value in enumerate(A[:-2]):
            # Find the difference between the start value and the next value
            # in the array.
            delta = A[start_index + 1] - start_value
            # Count the number of sequences of length greater than three
            # that start at start_index that have a common difference of
            # delta.
            for a, b in zip(A[start_index + 1:-1], A[start_index + 2:]):
                if b - a == delta:
                    # If the difference remains delta, then this is an 
                    # arithemetic sequence starting at start_index and
                    # ending where b is.
                    soln += 1
                else:
                    # If the difference is not delta, stop.
                    break
        return soln



def test_1():
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3

def test_2():
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4, 7, 8, 9, 10]) == 6

def test_3():
    assert Solution().numberOfArithmeticSlices([1, 2, 4, 5, 7, 8, 10, 11]) == 0

def test_4():
    assert Solution().numberOfArithmeticSlices([4, 3, 2, 1]) == 3
