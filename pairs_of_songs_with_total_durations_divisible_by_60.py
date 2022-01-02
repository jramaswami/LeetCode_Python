"""
LeetCode :: January 2022 Challenge :: 1010. Pairs of Songs With Total Durations Divisible by 60
jramaswami
"""


import collections


class Solution:

    def numPairsDivisibleBy60(self, song_times):
        freqs = collections.Counter(t % 60 for t in song_times)
        soln = 0
        for song_time in freqs:
            if song_time == 0 or song_time == 30:
                # Special case for duration % 60 = 0 and duration % 60 = 30:
                # n choose 2.
                n = freqs[song_time]
                soln += ((n * (n - 1)) // 2)
            else:
                # Otherwise, you can pair this with other songs that will cause
                # t[1] % 60 + t[2] % 60 == 60
                delta = 60 - song_time
                # To avoid double counting, only count when d > freqs[f]
                if delta > song_time and delta in freqs:
                    soln += (freqs[song_time] * freqs[delta])
        return soln


def test_1():
    song_times = [30,20,150,100,40]
    assert Solution().numPairsDivisibleBy60(song_times) == 3


def test_2():
    song_times = [60,60,60]
    assert Solution().numPairsDivisibleBy60(song_times) == 3
