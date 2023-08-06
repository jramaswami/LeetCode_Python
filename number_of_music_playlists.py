"""
LeetCode
920. Number of Music Playlists
August 2023 Challenge
jramaswami
"""


class Solution:
    def numMusicPlaylists(self, song_count: int, playlist_length: int, cycle_length: int) -> int:
        MOD = pow(10, 9) + 7
        # dp[playlist length][number of unique songs]
        dp = [[0 for _ in range(song_count+1)] for _ in range(playlist_length+1)]
        dp[0][0] = 1
        for p in range(playlist_length):
            for u in range(0, song_count+1):
                if dp[p][u] > 0:
                    # We exclude songs that are waiting to cycle.
                    # If the current playlist length, p, is less than the
                    # current cycle lenght, than we exclude p songs.
                    excluded = min(cycle_length, p)
                    # Compute the number of songs we can add to the playlist.
                    useable = song_count - excluded
                    # Compute how many of those songs are being added for the
                    # first time.
                    first_timers = song_count - u
                    # Compute how many of those songs are repeats.
                    repeats = useable - first_timers
                    # First timers add to the number of unique songs
                    if first_timers > 0:
                        k = (dp[p][u] * first_timers) % MOD
                        dp[p+1][u+1] = (dp[p+1][u+1] + k) % MOD
                    # Repeats do not add to the number of unique songs
                    if repeats > 0:
                        k = (dp[p][u] * repeats) % MOD
                        dp[p+1][u] = (dp[p+1][u] + k) % MOD
        return dp[playlist_length][song_count]



def test_1():
    n = 3
    goal = 3
    k = 1
    expected = 6
    assert Solution().numMusicPlaylists(n, goal, k) == expected


def test_2():
    n = 2
    goal = 3
    k = 0
    expected = 6
    assert Solution().numMusicPlaylists(n, goal, k) == expected


def test_3():
    n = 2
    goal = 3
    k = 1
    expected = 2
    assert Solution().numMusicPlaylists(n, goal, k) == expected