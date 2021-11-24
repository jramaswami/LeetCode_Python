"""
LeetCode :: November 2021 Challenge :: 986. Interval List Intersections
jramaswami
"""


class Solution:
    def intervalIntersection(self, firstList, secondList):

        def are_overlapping(int1, int2):
            return max(int1[0],int2[0]) <= min(int1[1], int2[1])

        def intersection(int1, int2):
            return [max(int1[0],int2[0]), min(int1[1], int2[1])]

        i = 0
        j = 0

        soln = []
        while i < len(firstList) and j < len(secondList):
            if are_overlapping(firstList[i], secondList[j]):
                soln.append(intersection(firstList[i], secondList[j]))

            # Jettison the first interval that is done.
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return soln


def test_1():
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    expected = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    assert Solution().intervalIntersection(firstList, secondList) == expected


def test_2():
    firstList = [[1,3],[5,9]]
    secondList = []
    expected = []
    assert Solution().intervalIntersection(firstList, secondList) == expected


def test_3():
    firstList = []
    secondList = [[4,8],[10,12]]
    expected = []
    assert Solution().intervalIntersection(firstList, secondList) == expected


def test_4():
    firstList = [[1,7]]
    secondList = [[3,10]]
    expected = [[3,7]]
    assert Solution().intervalIntersection(firstList, secondList) == expected