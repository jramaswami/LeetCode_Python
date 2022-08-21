"""
LeetCode :: August Challenge :: Stamping the Sequence
jramaswami

REF: https://www.youtube.com/watch?v=e3SR3NpebEU
"""


from typing import *


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        def matches(i):
            """
            Return True if you can stamp starting at i and get a match.
            Exclude a match that is all "?"s
            """
            found_nonq = False
            j = 0
            while j < len(stamp):
                # Stamp cannot go outside target.
                if i >= len(target):
                    return False
                if target[i] != '?' and target[i] != stamp[j]:
                    return False
                if target[i] != '?':
                    found_nonq = True
                i += 1
                j += 1
            return found_nonq

        def find_first_stamp():
            "Return the index of the first matching stamp."
            for i, _ in enumerate(target):
                if matches(i):
                    return i
            return -1

        def do_stamp(i):
            "Stamp starting at i."
            for j, _ in enumerate(stamp):
                if i + j >= len(target):
                    break
                target[i + j] = '?'

        soln = []
        x = 0
        while any(t != "?" for t in target):
            # Find first match of stamp.
            i = find_first_stamp()
            if i < 0:
                soln = []
                break
            soln.append(i)
            do_stamp(i)
            x += 1
            if x > 10 * len(target):
                soln = []
                break
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
    print(result)
    assert verify(result, target, stamp)


def test_5():
    "WA"
    stamp = "bedaefaeddccbce"
    target = "bebedabebbedaefaeddccbced"
    result = Solution().movesToStamp(stamp, target)
    # assert verify(result, target, stamp)
    assert result == []

def test_6():
    "WA"
    stamp = "v"
    target = "v"
    result = Solution().movesToStamp(stamp, target)
    # assert verify(result, target, stamp)
    assert result == [0]