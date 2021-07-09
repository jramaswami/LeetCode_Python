"""
Leet Code :: May 2021 Challenge :: Minimum Moves to Equal Array Elements II
jramaswami
"""
from typing import *
from math import ceil, floor


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums0 = sorted(nums)
        median_index  = len(nums0) // 2
        if len(nums0) % 2:
            median_index += 1
        median = nums0[len(nums0) // 2]
        return sum(abs(n - median) for n in nums)


def test_1():
    nums = [1,2,3]
    assert Solution().minMoves2(nums) == 2


def test_2():
    nums = [1,10,2,9]
    assert Solution().minMoves2(nums) == 16


def test_3():
    nums = [-54, -64, -100, -12, 88, -79, -14, -21, 94, 29, 4, 2, 72, 54, 91, -60, -99, -18, 80, 0]
    assert Solution().minMoves2(nums) == 1035


def test_4():
    nums = [99, 59, -77, -56, -96, -11, -61, 63, -15, 78, -77, -64, -69, -15, -69, -56, -56, -67, -2, 91, 67, -11, 60, -49, -40, 24, 86, -42, -67, 53, -1, -98, -40, -7, 79, -48, 31, 58, 10, 60, 55, -71, -12, 29, 31, 53, -86, -77, 31, -2, 25, -49, -57, -24, 79, 75, -91, -67, 66, -79, -36, -93, -11, 72, -68, 85, 39, -49, -48, -49, -53, 49, -31, -62, -42, 96, 61, 4, -37, 0, 70, -98, -13, 41, 2, -58, -6, -58, -13, -72, -77, -82, -95, 40, 7, -6, -83, -29, 65, -93, 63, -25, -92, 77, -82, 9, 56, 95, 1, 75, -33, -56, -31, -9, 70, 21, -53, -8, -3, 86, 34, 71, -90, -7, -87, 35, 93, -34, -40, -25, -36, -96, -11, 92, -21, -94, 44, 12, -59, 26, 83, 33, 31, 66, 77, 73, -26, 26, -9, 29, 93, 77, -56, -24, -56, 87, 33, 91, 65, -82, -94, 78, 52, -37, 65, 42, -89, 15, -88, 92, 56, -38, 5, -47, 41, -13, -91, 37, 66, -61, -88, -52, 40, -56, 78, -48, 86, -87, 96, 28, 52, 74, 13, -47, 38, 5, 85, -54, -86, -96]
    assert Solution().minMoves2(nums) == 10481


def test_5():
    nums = [-77, 56, 82, 65, -55, -16, 0, -4, 100, 39, 22, 42, -57, -97, -41, -72, -88, -76, -45, 70, 86, -37, 95, -10, -23, -42, 47, -49, -67, 60, 16, -70, 64, -4, 59, -21, 65, 91, 32, -32, -59, 19, -7, -12, 66, 54, -17, -21, 85, -91, -81, -85, -66, 69, -42, -13, 91, -76, 75, 81, -26, -53, 98, 71, 32, 40, -11, -79, -76, -44, -93, -84, -64, -47, 54, -20, -77, -95, 27, 69, 98, -56, 1, 82, 55, 77, 30, 66, -50, 77, -77, -75, 70, 47, 37, -17, 12, -90, 92, -74, 2, 3, -100, -27, -65, 21, -7, -55, 2, -38, -12, 20, -79, 3, -41, 12, 46, 31, 56, -27, -24, 52, 41, -73, -44, -90, 19, 78, 63, 54, 67, 28, 25, -53, -78, -22, -49, 91, 47, 95, 9, 7, 97, 16, -26, -14, -21, -72, -98, -62, -95, 77, 90, -46, 74, 92, 97, 46, 58, 12, -27, 43, -8, -47, 60, 80, 89, 91, 63, -39, -66, -49, -38, -29, -55, -14, -1, -22, 0, 27, 27, -55, 97, 96, 24, -42, 46, -72, -24, -61, 39, -20, -34, -13, -83, 88, -26, 7, 90, 20, -64]
    assert Solution().minMoves2(nums) == 10246


def test_6():
    nums = [-77, 56, 82, 65, -55, -16, 0, -8, 100, 39, 22, 42, -57, -97, -41, -72, -88, -76, -45, 70, 86, -37, 95, -10, -23, -42, 47, -49, -67, 60, 16, -70, 64, -4, 59, -21, 65, 91, 32, -32, -59, 19, -7, -12, 66, 54, -17, -21, 85, -91, -81, -85, -66, 69, -42, -13, 91, -76, 75, 81, -26, -53, 98, 71, 32, 40, -11, -79, -76, -44, -93, -84, -64, -47, 54, -20, -77, -95, 27, 69, 98, -56, 1, 82, 55, 77, 30, 66, -50, 77, -77, -75, 70, 47, 37, -17, 12, -90, 92, -74, 2, 3, -100, -27, -65, 21, -7, -55, 2, -38, -12, 20, -79, 3, -41, 12, 46, 31, 56, -27, -24, 52, 41, -73, -44, -90, 19, 78, 63, 54, 67, 28, 25, -53, -78, -22, -49, 91, 47, 95, 9, 7, 97, 16, -26, -14, -21, -72, -98, -62, -95, 77, 90, -46, 74, 92, 97, 46, 58, 12, -27, 43, -8, -47, 60, 80, 89, 91, 63, -39, -66, -49, -38, -29, -55, -14, -1, -22, 0, 27, 27, -55, 97, 96, 24, -42, 46, -72, -24, -61, 39, -20, -34, -13, -83, 88, -26, 7, 90, 20, -64]
    assert Solution().minMoves2(nums) == 10250