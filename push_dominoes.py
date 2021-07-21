"""
LeetCode :: July 2021 Challenge :: Push Dominoes
jramaswami
"""


from math import inf


class Solution:
    def pushDominoes(self, dominoes):
        falling_left = [0 for _ in dominoes]
        falling_right = [0 for _ in dominoes]

        # Falling to the right.  O(N)
        curr = inf
        for i in range(len(dominoes)):
            if curr < inf and dominoes[i] == '.':
                curr += 1
            elif dominoes[i] == 'R':
                curr = 1
            elif dominoes[i] == 'L':
                curr = inf
            falling_right[i] = curr

        # Falling to the left.  O(N)
        curr = inf
        for i in range(len(dominoes)-1, -1, -1):
            if curr < inf and dominoes[i] == '.':
                curr += 1
            elif dominoes[i] == 'L':
                curr = 1
            elif dominoes[i] == 'R':
                curr = inf
            falling_left[i] = curr

        # The kind of push that arrives first is the push that goes in the
        # solution.  If the two pushes arrive at the same time, then they
        # will (or both don't arrive at all) then they cancel.
        soln = []
        for l, r in zip(falling_left, falling_right):
            if l < r:
                soln.append('L')
            elif l > r:
                soln.append('R')
            else:
                soln.append('.')
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
