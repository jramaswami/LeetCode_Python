"""
LeetCode :: 1323. Maximum 69 Number
November 2022 Challenge
"""


class Solution:

    def maximum69Number(self, num: int) -> int:
        return int((str(num)).replace("6", "9", 1))


def test_1():
    num = 9669
    expected = 9969
    assert Solution().maximum69Number(num) == expected


def test_2():
    num = 9996
    expected = 9999
    assert Solution().maximum69Number(num) == expected


def test_3():
    num = 9999
    expected = 9999
    assert Solution().maximum69Number(num) == expected