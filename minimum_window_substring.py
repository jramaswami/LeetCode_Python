"""
LeetCode :: August 2021 Challenge :: Minimum Window Substring
jramaswami
"""


import collections


Letter = collections.namedtuple('Letter', ['letter', 'index'])


class Solution:
    def minWindow(self, S, T):
        # Get the required frequency of each letter in T.
        freqs = collections.defaultdict(int)
        for c in T:
            freqs[c] += 1

        # We will keep track of the letters and their indexes in a queue.
        letters = collections.deque()

        # Initial solution is ""
        min_length = len(S) + 1
        soln = ""

        for i, c in enumerate(S):
            # Only process letters that are in T.
            if c in freqs:
                freqs[c] -= 1
                letters.append(Letter(c, i))

            # If we have enough of every letters ...
            while all(f <= 0 for c, f in freqs.items()):
                # See if this is the smallest substring.
                left = letters[0].index
                right = letters[-1].index
                if (right - left + 1) < min_length:
                    min_length, soln = (right - left + 1), S[left:right+1]

                # Remove letters that allow the freqs to remain high enough.
                d = letters[0].letter
                if freqs[d] <= 0:
                    freqs[d] += 1
                    letters.popleft()

        return soln


def test_1():
    S = "ADOBECODEBANC"
    T = "ABC"
    expected = "BANC"
    assert Solution().minWindow(S, T) == expected


def test_2():
    S = "a"
    T = "a"
    expected = "a"
    assert Solution().minWindow(S, T) == expected


def test_3():
    S = "a"
    T = "aa"
    expected = ""
    assert Solution().minWindow(S, T) == expected
