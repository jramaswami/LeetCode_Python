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
    def merge(A, aux, left, mid, right):
        inversions = 0
        left_p = left
        right_p = mid + 1
        aux_p = left
        while left_p <= mid and right_p <= right:
            if A[left_p] <= A[right_p]:
                aux[aux_p] = A[left_p]
                left_p += 1
                aux_p += 1
            else: 
                aux[aux_p] = A[right_p]
                inversions += (mid - left_p + 1)
                right_p += 1
                aux_p += 1

        while left_p <= mid:
            aux[aux_p] = A[left_p]
            left_p += 1
            aux_p += 1

        while right_p <= right:
            aux[aux_p] = A[right_p]
            right_p += 1
            aux_p += 1

        for aux_p in range(left, right + 1):
            A[aux_p] = aux[aux_p]

        return inversions

    def mergesort(A, aux, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        inversions = mergesort(A, aux, left, mid)
        inversions += mergesort(A, aux, mid + 1, right)
        inversions += merge(A, aux, left, mid, right)
        return inversions

    A0 = list(A)
    aux = list(A)
    soln = mergesort(A0, aux, 0, len(A0) - 1)
    return soln


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
