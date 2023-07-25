"""
LeetCode
852. Peak Index in a Mountain Array
July 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 1
        hi = len(arr) - 2
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                # Peak
                return mid
            elif arr[mid-1] < arr[mid]:
                # Array increasing but not peak, so try to the right.
                lo = mid + 1
            elif arr[mid] > arr[mid+1]:
                # Array decreasing but not peak, so try to the left.
                hi = mid - 1
            else:
                raise Exception(f"Unexpected case {arr=} {mid=}")
        raise Exception("No peak found.")


def test_1():
    arr = [0,1,0]
    expected = 1
    assert Solution().peakIndexInMountainArray(arr) == expected


def test_2():
    arr = [0,2,1,0]
    expected = 1
    assert Solution().peakIndexInMountainArray(arr) == expected


def test_3():
    arr = [0,10,5,2]
    expected = 1
    assert Solution().peakIndexInMountainArray(arr) == expected