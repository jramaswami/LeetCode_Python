"""
LeetCode :: March 2022 Challenge :: Two City Scheduling
jramaswami
"""


import functools
import math


class Solution:
    def twoCitySchedCost(self, costs):
        LIMIT = len(costs) // 2

        @functools.cache
        def solve(a, b):
            if a > LIMIT:
                return math.inf
            if b > LIMIT:
                return math.inf
            if a == LIMIT and b == LIMIT:
                return 0
            i = a + b
            return min(
                costs[i][0] + solve(a+1, b),
                costs[i][1] + solve(a, b+1)
            )

        return solve(0, 0)


def test_1():
    costs = [[10,20],[30,200],[400,50],[30,20]]
    expected = 110
    assert Solution().twoCitySchedCost(costs) == expected


def test_2():
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    expected = 1859
    assert Solution().twoCitySchedCost(costs) == expected


def test_3():
    costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    expected = 3086
    assert Solution().twoCitySchedCost(costs) == expected


def test_4():
    costs = [[646, 806], [508, 901], [917, 31], [550, 90], [317, 831], [978, 566], [750, 269], [631, 688], [686, 910], [689, 28], [660, 317], [938, 39], [501, 29], [194, 213], [572, 90], [657, 32], [146, 170], [151, 697], [380, 508], [402, 226], [304, 454], [511, 350], [485, 324], [771, 162], [202, 551], [719, 478], [281, 714], [97, 491], [149, 129], [266, 34], [322, 892], [495, 817], [928, 755], [741, 539], [280, 154], [805, 538], [342, 928], [147, 22], [571, 702], [621, 363], [6, 170], [894, 350], [605, 346], [578, 711], [536, 160], [78, 570], [654, 223], [357, 194], [161, 352], [739, 993], [355, 284], [403, 344], [732, 6], [236, 225], [81, 589], [349, 411], [997, 209], [491, 445], [312, 328], [413, 158], [546, 587], [892, 97], [178, 25], [286, 787], [312, 747], [314, 982], [382, 811], [641, 376], [660, 710], [605, 263], [487, 754], [772, 664], [413, 886], [65, 85], [219, 941], [385, 786], [572, 515], [517, 3], [531, 23], [35, 908], [981, 473], [661, 306], [339, 706], [440, 24], [793, 943], [803, 651], [837, 696], [143, 907], [820, 509], [934, 174], [356, 531], [148, 737], [655, 338], [470, 585], [740, 138], [510, 37], [598, 171], [572, 354], [12, 881], [605, 699]]
    expected = 30086
    assert Solution().twoCitySchedCost(costs) == expected
