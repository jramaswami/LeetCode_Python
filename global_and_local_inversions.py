"""
LeetCode :: April 2021 Challenge :: Global and Local Inversions
jramaswami
"""
from typing import *


def count_local_inversions(A):
    """
    The number of local inversions is the number of i with 0 <= i < N 
    and A[i] > A[i+1].
    """
    return sum(1 if ai > aj else 0 for ai, aj in zip(A[:-1], A[1:]))


def count_global_inversions(A):
    """
    The number of (global) inversions is the number of i < j 
    with 0 <= i < j < N and A[i] > A[j].
    """
    inversions = 0
    for i, a in enumerate(A):
        if i > a:
            inversions += i - a
    return inversions


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return count_local_inversions(A) == count_global_inversions(A)


#
# TESTING
#
def test_1():
    A = [1,0,2]
    assert Solution().isIdealPermutation(A) == True

def test_2():
    A = [1,2,0]
    assert Solution().isIdealPermutation(A) == False

def test_3():
    A = [9, 3, 1, 5, 4, 6, 2, 7, 0, 8]
    assert Solution().isIdealPermutation(A) == False

def test_4():
    A = [32, 20, 10, 28, 34, 4, 8, 43, 21, 7, 27, 25, 40, 1, 41, 5, 48, 46, 24, 16, 23, 29, 3, 17, 2, 47, 14, 44, 38, 45, 12, 36, 26, 0, 9, 15, 13, 37, 39, 22, 42, 11, 18, 30, 49, 19, 31, 6, 35, 33]
    assert Solution().isIdealPermutation(A) == False

def test_5():
    A = [0, 2, 1, 3, 4, 5, 7, 6, 9, 8]
    assert Solution().isIdealPermutation(A) == True

def test_6():
    """WA"""
    A = [2,1,0]
    assert Solution().isIdealPermutation(A) == False

def main():
    """Main program.  Generate a list where local inversions == global inversions."""
    import random
    A = list(range(10))
    random.shuffle(A)
    while count_local_inversions(A) != count_global_inversions(A):
        random.shuffle(A)
    print(A)


if __name__ == '__main__':
    main()
