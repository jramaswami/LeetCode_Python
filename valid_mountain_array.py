"""
LeetCode :: Array Module :: Valid Mountain Array
jramaswami
"""

class Solution:
    def validMountainArray(self, arr):
        # (1) len(arr) >= 3
        if len(arr) < 3:
            return False

        # (2) there exists an i with 0 < i < len(arr) - 1 such that
        #     (a) arr[0] < arr[1] < ... < arr[i-1] < arr[i]
        #     (b) arr[i] > arr[i+1] > ... > arr[len(arr)-1]
        i = 0
        while i < len(arr) and arr[i] < arr[i+1]:
            i += 1
        j = len(arr) - 1
        while j >= 0 and arr[j-1] > arr[j]:
            j -= 1
        return i == j


def test_1():
    arr = [2, 1]
    assert Solution().validMountainArray(arr) == False


def test_2():
    arr = [3, 5, 5]
    assert Solution().validMountainArray(arr) == False


def test_3():
    arr = [0, 3, 2, 1]
    assert Solution().validMountainArray(arr) == True


def test_4():
    arr = []
    assert Solution().validMountainArray(arr) == False


def test_5():
    arr = [0, 1, 2, 3, 4, 3, 2, 1, 0, 0]
    assert Solution().validMountainArray(arr) == False


def test_6():
    arr = [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1]
    assert Solution().validMountainArray(arr) == False


def test_7():
    """RTE"""
    arr = [0,1,2,3,4,5,6,7,8,9]
    assert Solution().validMountainArray(arr) == False
