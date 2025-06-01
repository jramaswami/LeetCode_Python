"""
LeetCode
2929. Distribute Candies Among Children II
June 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        x = 1
        incr = 1
        window = collections.deque((0 for _ in range(limit+1)))
        curr_sum = 0
        for i in range(n+1):
            # Add x to window and curr_sum
            window.append(x)
            curr_sum += x
            x += incr
            x = max(x, 0)
            if x == limit + 1:
                incr = -1
            # Remove any expired elements
            while len(window) > limit + 1:
                curr_sum -= window[0]
                window.popleft()
        return curr_sum


def test_1():
    n = 5
    limit = 2
    assert Solution().distributeCandies(n, limit) == 3


def test_2():
    n = 3
    limit = 3
    assert Solution().distributeCandies(n, limit) == 10


def test_3():
    n = 10001
    limit = 20001
    assert Solution().distributeCandies(n, limit) == 50025003