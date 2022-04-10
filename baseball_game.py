"""
LeetCode :: April 2022 Challenge :: 682. Baseball Game
jramaswami
"""


class Solution:

    def calPoints(self, ops):
        record = []
        for op in ops:
            if op == '+':
                record.append(record[-2] + record[-1])
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                record.pop()
            else:
                n = int(op)
                record.append(n)
        return sum(record)


def test_1():
    ops = ["5","2","C","D","+"]
    expected = 30
    assert Solution().calPoints(ops) == expected


def test_2():
    ops = ["5","-2","4","C","D","9","+","+"]
    expected = 27
    assert Solution().calPoints(ops) == expected


def test_3():
    ops = ["1"]
    expected = 1
    assert Solution().calPoints(ops) == expected
