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
            return bs

        def validate_char(char):
            if len(char) == 1:
                return True
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
            if mask & char[0] != expected:
                # print(f"Header 1: {len(A)} {char[0]:08b}")
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
