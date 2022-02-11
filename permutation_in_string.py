"""
LeetCode :: February 2022 Challenge :: 567. Permutation in String
jramaswami
"""


import collections
import string


class Solution:

    def checkInclusion(self, s1, s2):
        # Initialize each to the same baseline of 1 for every letter.
        target_ctr = collections.Counter(string.ascii_lowercase)
        window_ctr = collections.Counter(string.ascii_lowercase)
        # Update with target string and initial sliding window, respectively.
        target_ctr.update(s1)
        window_ctr.update(s2[:len(s1)])
        # Use a sliding window to find if there is a permuation present.
        # Check intial window.
        if target_ctr == window_ctr:
            return True
        for i, _ in enumerate(s2[len(s1):], start=len(s1)):
            window_ctr[s2[i-len(s1)]] -= 1
            window_ctr[s2[i]] += 1
            if target_ctr == window_ctr:
                return True
        return False


def test_1():
    s1 = "ab"
    s2 = "eidbaooo"
    expected = True
    assert Solution().checkInclusion(s1, s2) == expected


def test_2():
    s1 = "ab"
    s2 = "eidboaoo"
    expected = False
    assert Solution().checkInclusion(s1, s2) == expected


def test_3():
    "WA"
    s1 = "adc"
    s2 = "dcda"
    expected = True
    assert Solution().checkInclusion(s1, s2) == expected
