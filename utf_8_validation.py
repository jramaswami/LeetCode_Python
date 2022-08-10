"""
LeetCode :: 393. UTF-8 Validation
jramaswami
"""


from typing import *


class Solution:

    def validUtf8(self, data: List[int]) -> bool:
        def expected_bytes(k):
            mask = (1 << 7)
            if mask & k == 0:
                return 1
            bs = 0
            for b in range(7, 3, -1):
                if (1 << b) & k:
                    bs += 1
                else:
                    break
            return bs

        def validate_char(char):
            # For n-bytes chars the first byte must have
            # n 1-bits followed by a 0-bit
            # The rest of the bits must start with 10
            if len(char) == 4:
                mask = int("11111000", 2)
                expected = int("11110000", 2)
            elif len(char) == 3:
                mask = int("11110000", 2)
                expected = int("11100000", 2)
            elif len(char) == 2:
                mask = int("11100000", 2)
                expected = int("11000000", 2)
            elif len(char) == 1:
                mask = int("10000000", 2)
                expected = int("00000000", 2)
            if mask & char[0] != expected:
                # print(f"Header 1: {len(char)} {char[0]:08b}")
                return False
            mask = int("11000000", 2)
            expected = int("10000000", 2)
            for c in char[1:]:
                if mask & c != expected:
                    # print(f"Header 2: {c:08b}")
                    return False
            return True

        chars = []
        i = 0
        while i < len(data):
            b = expected_bytes(data[i])
            chars.append(data[i:i+b])
            # Make sure we got enough bytes.
            if len(chars[-1]) != b:
                return False
            i += b
        return all(validate_char(c) for c in chars)



def test_1():
    data = [197,130,1]
    expected = True
    assert Solution().validUtf8(data) == expected


def test_2():
    data = [235,140,4]
    expected = False
    assert Solution().validUtf8(data) == expected


def test_3():
    "WA"
    data = [235]
    expected = False
    assert Solution().validUtf8(data) == expected


def test_4():
    "WA"
    data = [194,155,231,184,185,246,176,131,161,222,174,227,162,134,241,154,168,185,218,178,229,187,139,246,178,187,139,204,146,225,148,179,245,139,172,134,193,156,233,131,154,240,166,188,190,216,150,230,145,144,240,167,140,163,221,190,238,168,139,241,154,159,164,199,170,224,173,140,244,182,143,134,206,181,227,172,141,241,146,159,170,202,134,230,142,163,244,172,140,191]
    expected = True
    assert Solution().validUtf8(data) == expected


def test_5():
    "WA"
    data = [145]
    print(f"{145:08b}")
    expected = False
    assert Solution().validUtf8(data) == expected
