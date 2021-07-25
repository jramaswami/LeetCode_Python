"""
LeetCode :: Array Module :: Check If N and Its Double Exist
jramaswami
"""

class Solution:
    def checkIfExist(self, arr):
        # The module only speaks about linear searching.  The constraints say
        # that len(arr) <= 500.  An O(N^2) algorithm should be fast enough.
        for i, n in enumerate(arr):
            for j, m in enumerate(arr):
                if i != j and n * 2 == m:
                    return True
        return False


def test_1():
    arr = [10, 2, 5, 3]
    assert Solution().checkIfExist(arr) == True


def test_2():
    arr = [7, 1, 14, 11]
    assert Solution().checkIfExist(arr) == True


def test_3():
    arr = [3, 1, 7, 11]
    assert Solution().checkIfExist(arr) == False


def test_4():
    arr = []
    assert Solution().checkIfExist(arr) == False


def test_5():
    """WA: The 0 dupes.  Check the index!"""
    arr = [-2,0,10,-19,4,6,-8]
    assert Solution().checkIfExist(arr) == False
