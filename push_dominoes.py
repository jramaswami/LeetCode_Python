"""
LeetCode :: September 2022 Challenge :: Push Dominoes
jramaswami
"""


import math


class Solution:
    def pushDominoes(self, dominoes):
        # Compute distance to right push. math.inf means no right push.
        curr = math.inf
        falling_right = [math.inf for _ in dominoes]
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                curr = 0
            elif dominoes[i] == '.':
                curr += 1
            else:
                curr = math.inf
            falling_right[i] = curr

        # Compute distance to left push. math.inf means no left push.
        curr = math.inf
        falling_left = [math.inf for _ in dominoes]
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == 'L':
                curr = 0
            elif dominoes[i] == '.':
                curr += 1
            else:
                curr = math.inf
            falling_left[i] = curr

        # Nearest push wins.  A tie means domino remains standing.
        soln = list(dominoes)
        for i, _ in enumerate(dominoes):
            if dominoes[i] == '.':
                if falling_left[i] < falling_right[i]:
                    soln[i] = 'L'
                elif falling_left[i] > falling_right[i]:
                    soln[i] = 'R'
        return "".join(soln)


def test_1():
    dominoes = "RR.L"
    expected = "RR.L"
    assert Solution().pushDominoes(dominoes) == expected


def test_2():
    dominoes = ".L.R...LR..L.."
    expected = "LL.RR.LLRRLL.."
    assert Solution().pushDominoes(dominoes) == expected


def test_3():
    dominoes = ""
    expected = ""
    assert Solution().pushDominoes(dominoes) == expected


def test_4():
    dominoes = "L"
    expected = "L"
    assert Solution().pushDominoes(dominoes) == expected


def test_5():
    dominoes = "R"
    expected = "R"
    assert Solution().pushDominoes(dominoes) == expected


def test_6():
    dominoes = "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
    expected = "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
    assert Solution().pushDominoes(dominoes) == expected
