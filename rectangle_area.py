"""
LeetCode :: 223. Rectangle Area
November 2022 Challenge
jramaswami
"""


def intersection_length(left1, right1, left2, right2):
    "Return length of intersection of two lines."
    #######
      ###
    if left1 <= left2 <= right1 and left1 <= right2 <= right1:
        return right2 - left2

      ###
    #######
    if left2 <= left1 <= right2 and left2 <= right1 <= right2:
        return right1 - left1

    ######
    ######
    if (left1 == left2 and right1 == right2):
        return right1 - left1

    ######
       ######
    if left1 <= left2 <= right1:
        return right1 - left2

       ######
    ######
    if left2 <= left1 <= right2:
        return right2 - left1

    # Not overlapping
    return 0


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1 = (ax2 - ax1) * (ay2 - ay1)
        rect2 = (bx2 - bx1) * (by2 - by1)
        print(intersection_length(ax1, ax2, bx1, bx2), intersection_length(ay1, ay2, by1, by2))
        intersect = intersection_length(ax1, ax2, bx1, bx2) * intersection_length(ay1, ay2, by1, by2)
        return rect1 + rect2 - intersect



def test_1():
    ax1 = -3
    ay1 = 0
    ax2 = 3
    ay2 = 4
    bx1 = 0
    by1 = -1
    bx2 = 9
    by2 = 2
    expected = 45
    assert Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected


def test_2():
    ax1 = -2
    ay1 = -2
    ax2 = 2
    ay2 = 2
    bx1 = -2
    by1 = -2
    bx2 = 2
    by2 = 2
    expected = 16
    assert Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected


def test_3():
    "WA"
    ax1 = 0
    ay1 = 0
    ax2 = 0
    ay2 = 0
    bx1 = -1
    by1 = -1
    bx2 = 1
    by2 = 1
    expected = 4
    assert Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected
