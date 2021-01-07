"""
leetcode :: 1640. Check Array Formation Through Concatenation
jramaswami
"""
from typing import *


def bin_search(a, pieces):
    """Binary search to find the piece that starts with a."""
    low = 0
    high = len(pieces) - 1
    while low <= high:
        mid = (low + high) // 2
        if pieces[mid][0] == a:
            return mid
        elif pieces[mid][0] < a:
            low = mid + 1
        else:
            high = mid - 1
    return -1


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces.sort()
        i = 0
        while i < len(arr):
            j = bin_search(arr[i], pieces)
            if j == -1:
                return False
            else:
                # Check to make sure that it all fits
                for v in pieces[j]:
                    if v != arr[i]:
                        return False
                    i += 1
        return True


def test_1():
    assert Solution().canFormArray([85], [[85]]) == True

def test_2():
    assert Solution().canFormArray([15, 88], [[88], [15]]) == True

def test_3():
    assert Solution().canFormArray([49,18,16], [[16,18,49]]) == False

def test_4():
    assert Solution().canFormArray([91,4,64,78], [[78],[4,64],[91]]) == True
