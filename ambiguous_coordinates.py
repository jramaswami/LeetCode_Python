"""
Leet Code :: May 2021 Challenge :: Ambiguous Coordinates
jramaswami
"""
from typing import *
from itertools import product


def add_decimal(numbers):
    """Add the decimal in a valid place."""
    result = []

    if numbers == ['0']:
        return numbers

    # Just in case, but it shouldn't happen.
    if len(numbers) > 1 and numbers[0] == '0' and numbers[-1] == '0':
        return result

    # If the last digit is 0 then this can only be an integer otherwise
    # it would have an extraneous trailing zero.
    if numbers[0] != '0':
        result.append("".join(numbers))

    if len(numbers) > 1 and numbers[-1] == '0':
        return result

    # If the number has a leading zero, then it can only be 0.xxxx
    # otherwise it would have an extraneous leading zero.
    if len(numbers) > 1:
        result.append("".join(numbers[:1] + ["."] + numbers[1:]))
    if numbers[0] == '0':
        return result

    for di in range(2, len(numbers)):
        result.append("".join(numbers[:di] + ["."] + numbers[di:]))

    return result



class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        soln = []
        numbers = [c for c in s][1:-1]
        for split in range(1, len(numbers)):
            left, right = numbers[:split], numbers[split:]
            # You cannot have too many leading zeros.
            if len(left) > 1 and left[0] == '0' and left[-1] == '0':
                continue
            if len(right) > 1 and right[0] == '0' and right[-1] == '0':
                continue

            left_numbers = add_decimal(left)
            right_numbers = add_decimal(right)

            if left_numbers and right_numbers:
                soln.extend(product(left_numbers, right_numbers))

        soln = ["(" + ", ".join([a, b]) + ")" for a, b in soln]
        return soln


def test_1():
    s = "(123)"
    expected = ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
    assert sorted(Solution().ambiguousCoordinates(s)) == sorted(expected)


def test_2():
    s = "(00011)"
    expected = ["(0.001, 1)", "(0, 0.011)"]
    assert sorted(Solution().ambiguousCoordinates(s)) == sorted(expected)


def test_3():
    s = "(0123)"
    expected = ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
    assert sorted(Solution().ambiguousCoordinates(s)) == sorted(expected)


def test_4():
    s = "(100)"
    expected = ['(10, 0)']
    assert sorted(Solution().ambiguousCoordinates(s)) == sorted(expected)


def test_5():
    s = "(00234502903)"
    expected = ["(0, 0.234502903)","(0.02, 3.4502903)","(0.02, 34.502903)","(0.02, 345.02903)","(0.02, 3450.2903)","(0.02, 34502.903)","(0.02, 345029.03)","(0.02, 3450290.3)","(0.02, 34502903)","(0.023, 4.502903)","(0.023, 45.02903)","(0.023, 450.2903)","(0.023, 4502.903)","(0.023, 45029.03)","(0.023, 450290.3)","(0.023, 4502903)","(0.0234, 5.02903)","(0.0234, 50.2903)","(0.0234, 502.903)","(0.0234, 5029.03)","(0.0234, 50290.3)","(0.0234, 502903)","(0.02345, 0.2903)","(0.0234502, 9.03)","(0.0234502, 90.3)","(0.0234502, 903)","(0.02345029, 0.3)"]
    assert sorted(Solution().ambiguousCoordinates(s)) == sorted(expected)


def test_6():
    s = "(325247000)"
    expected = ["(3, 25247000)","(3.2, 5247000)","(32, 5247000)","(3.25, 247000)","(32.5, 247000)","(325, 247000)","(3.252, 47000)","(32.52, 47000)","(325.2, 47000)","(3252, 47000)","(3.2524, 7000)","(32.524, 7000)","(325.24, 7000)","(3252.4, 7000)","(32524, 7000)","(32524700, 0)"]
    assert sorted(Solution().ambiguousCoordinates(s)) == sorted(expected)
