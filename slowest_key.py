"""
LeetCode :: September 2021 Challenge :: Slowest Key
jramaswami
"""


class Solution:
    def slowestKey(self, release_times, keys_pressed):
        max_time = 0
        max_key = None
        for i, (rtime, key) in enumerate(zip(release_times, keys_pressed)):
            delta = rtime
            if i > 0:
                delta = rtime - release_times[i-1]
            if delta > max_time:
                max_time, max_key = delta, key
            elif delta == max_time:
                max_key = max(key, max_key)
        return max_key


def test_1():
    release_times = [9,29,49,50]
    keys_pressed = "cbcd"
    assert Solution().slowestKey(release_times, keys_pressed) == "c"


def test_2():
    release_times = [12,23,36,46,62]
    keys_pressed = "spuda"
    assert Solution().slowestKey(release_times, keys_pressed) == "a"
