"""
LeetCode :: June 2021 Challenge :: Maximum Units on a Truck
jramaswami
"""


from typing import *


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        NUMBER_OF_BOXES = 0
        UNITS_PER_BOX = 1
        boxTypes0 = sorted(boxTypes, key=lambda box: box[UNITS_PER_BOX])
        units_in_truck = 0
        while boxTypes0 and truckSize:
            boxes_to_take = min(truckSize, boxTypes0[-1][NUMBER_OF_BOXES])
            truckSize -= boxes_to_take
            units_in_truck += (boxes_to_take * boxTypes0[-1][UNITS_PER_BOX])
            boxTypes0.pop()
        return units_in_truck


def test_1():
    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4
    expected = 8
    assert Solution().maximumUnits(boxTypes, truckSize) == expected


def test_2():
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    expected = 91
    assert Solution().maximumUnits(boxTypes, truckSize) == expected
