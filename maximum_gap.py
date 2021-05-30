"""
LeetCode :: May 2021 Challenge :: Maximum Gap
jramaswami
"""


from typing import *
from math import inf


def radix_sort(nums):
    """
    Sort nums using a radix sort.
    Sorts in linear time with extra space proportional to N.
    """
    # Do not mutate nums
    nums0 = list(nums)
    # Auxilliary array for radix sort
    aux = list(nums0)
    # Radix sort (binary)
    for bit in range(31):
        mask = 1 << bit
        ones_index = sum(0 if n & mask else 1 for n in nums0)
        zeros_index = 0
        # Copy numbers into aux in a stable way
        for n in nums0:
            if n & mask:
                aux[ones_index] = n
                ones_index += 1
            else:
                aux[zeros_index] = n
                zeros_index += 1
        # Copy numbers back into nums0
        for i, n in enumerate(aux):
            nums0[i] = n

    return nums0


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Base case
        if len(nums) < 2:
            return 0

        nums0 = radix_sort(nums)
        return max(b - a for a, b in zip(nums0, nums0[1:]))


#
# Testing
#

from random import randint


def test_radix_sort():
    N = pow(10, 4)
    min_n, max_n = 0, pow(10, 9)
    for _ in range(10):
        A = [randint(min_n, max_n) for _ in range(N)]
        B = sorted(A)
        C = radix_sort(A)
        assert B == C


def test_1():
    nums = [3,6,9,1]
    assert Solution().maximumGap(nums) == 3


def test_2():
    nums = [10]
    assert Solution().maximumGap(nums) == 0


def test_3():
    nums = [837015319, 63504682, 616194255, 185679165, 742351974, 916785397,
            994946433, 52774335, 753327058, 903933578, 29336478, 976840453,
            38903762, 875238420, 230558891, 261093225, 941081231, 541725611,
            674265039, 889382990, 732620749, 490670483, 933604114, 38228976,
            103649735, 675883821, 759615323, 593014710, 293236943, 80693193,
            648590315, 543502497, 131596304, 780829479, 564735931, 477653169,
            722074353, 648101154, 64598176, 915630964, 541344586, 754559624,
            789625869, 369274648, 406717810, 297558976, 506162, 794632303,
            443369722, 426518403, 276978979, 13694517, 107202129, 348767771,
            575306519, 878211357, 415402275, 459911638, 98124379, 185422550,
            503794356, 720420919, 329909920, 975949755, 818040772, 49713832,
            231746822, 214184991, 903602455, 203364523, 803021901, 597893178,
            210575625, 752085924, 185095562, 172762828, 193800954, 814814575,
            766297972, 7899216, 86359657, 522715003, 137407682, 574455762,
            485949004, 126105266, 224030888, 240624739, 160026560, 630338802,
            811747902, 85287056, 153715637, 238057113, 464988403, 804640746,
            923629363, 422614035, 706863466, 488361434]
    assert Solution().maximumGap(nums) == 38223101