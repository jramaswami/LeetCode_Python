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
            for j, b in enumerate(target[i:], start=i):
                if j - i >= len(stamp):
                    break
                a = stamp[j-i]
                if b != "?" and a != b:
                    return False
                if b != "?":
                    found_nonq = True
            return found_nonq

        def find_first_stamp():
            "Return the index of the first matching stamp."
            print(f"find_first_stamp() {stamp=} {''.join(target)}")
            for i, _ in enumerate(target[:-len(stamp)+1]):
                print(i, "".join(target[i:]))
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
            print("".join(target), i)
            if i < 0:
                soln = []
                break
            soln.append(i)
            do_stamp(i)
            x += 1
            if x > 10 * len(target):
                soln = []
                break
        print("".join(target), stamp)
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