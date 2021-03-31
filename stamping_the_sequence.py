"""
LeetCode :: March 2021 Challenge :: Stamping the Sequence
jramaswami
"""
from typing import *


def left_match(target_index, target, stamp):
    """Can you match left to right?"""
    ok = False
    for i, _ in enumerate(stamp):
        if target_index + i >= len(target):
            return False

        if target[target_index + i] == '?':
            continue
        else:
            ok = True
        if stamp[i] != target[target_index + i]:
            return False
    return ok and True


def right_match(target_index, target, stamp):
    """Can you match right to left?"""
    ok = False
    for off, _ in enumerate(stamp):
        if target_index - off < 0:
            return False
        if target[target_index - off] == '?':
            continue
        else:
            ok = True
        if stamp[len(stamp) - off - 1] != target[target_index - off]:
            return False
    return ok and True


def question_from_left(target_index, target, stamp):
    """Replace chars with questions marks left to right."""
    replacements = 0
    for i, _ in enumerate(stamp):
        if target[target_index + i] != "?":
            target[target_index + i] = "?"
            replacements += 1
    return replacements


def question_from_right(target_index, target, stamp):
    """Replace chars with questions marks right to left."""
    replacements = 0
    for i, _ in enumerate(stamp):
        if target[target_index - i] != "?":
            target[target_index - i] = "?"
            replacements += 1
    return replacements


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target0 = list(target)
        soln = []
        questions = 0
        while questions < len(target0):
            found = False
            for target_index, _ in enumerate(target0):
                if left_match(target_index, target0, stamp):
                    found = True
                    soln.append(target_index)
                    questions += question_from_left(target_index, target0, stamp)
                elif right_match(target_index, target0, stamp):
                    found = True
                    soln.append(target_index - len(stamp) + 1)
                    questions += question_from_right(target_index, target0, stamp)
            if not found:
                return []
        return soln[::-1]


# 
# TESTING
#
def verify(stamp_indices, target, stamp):
    result = ["?" for _ in target]
    for stamp_index in stamp_indices:
        for off, c in enumerate(stamp):
            result[stamp_index + off] = c
    return "".join(result) == target


def test_1():
    stamp = "abc"
    target = "ababc"
    result = Solution().movesToStamp(stamp, target)
    assert verify(result, target, stamp)


def test_2():
    stamp = "abca"
    target = "aabcaca"
    result = Solution().movesToStamp(stamp, target)
    assert verify(result, target, stamp)


def test_3():
    """TLE"""
    stamp = "aye"
    target = "eyeye"
    result = Solution().movesToStamp(stamp, target)
    assert result == []


def test_4():
    """WA"""
    stamp = "zbs"
    target = "zbzbsbszbssbzbszbsss"
    result = Solution().movesToStamp(stamp, target)
    assert verify(result, target, stamp)
