"""
LeetCode :: May 2022 Challenge :: Check If a String Contains All Binary Codes of Size K
jramaswami
"""


class Solution:
    def hasAllCodes(self, s, k):
        has_code = [False for _ in range(pow(2, k))]

        # Initialize first window. Note: codes are backwards but that
        # does not make any difference to problem.
        window_code = 0
        mask = 1 << (k - 1)
        for i in range(k):
            window_code >>= 1
            if s[i] == '1':
                window_code |= mask
        has_code[window_code] = True

        # Sliding window.
        for i in range(k, len(s)):
            window_code >>= 1
            if s[i] == '1':
                window_code |= mask
            has_code[window_code] = True

        return all(has_code)


def test_1():
    assert Solution().hasAllCodes("00110", 2) == True


def test_2():
    assert Solution().hasAllCodes("0110", 1) == True


def test_3():
    assert Solution().hasAllCodes("0110", 2) == False


def test_4():
    assert Solution().hasAllCodes("0000000001011100", 4) == False


def test_5():
    "RTE"
    assert Solution().hasAllCodes("0", 20) == False
