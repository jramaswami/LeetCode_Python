"""
LeetCode :: Arrays Module :: Replace Elements with Greatest Element on Right Side
jramaswami
"""


class Solution:
    def replaceElements(self, arr):
        # Normally I would not do this in-place, but this is in the in-place
        # section of the module.
        next_max = curr_max = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            next_max = max(curr_max, arr[i])
            arr[i] = curr_max
            curr_max = next_max
        arr[-1] = -1
        return arr


def test_1():
    arr = [17,18,5,4,6,1]
    expected = [18,6,6,6,1,-1]
    assert Solution().replaceElements(arr) == expected


def test_2():
    arr = [400]
    expected = [-1]
    assert Solution().replaceElements(arr) == expected
