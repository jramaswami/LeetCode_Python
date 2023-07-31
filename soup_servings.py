"""
LeetCode
808. Soup Servings
July 2023 Challenge
jramaswami
"""


import collections


EPS = pow(10, -5)



class Solution:
    def soupServings(self, n: int) -> float:
        # Per discussion
        if n >= 4800:
            return 1.0

        ops = ((-100, 0), (-75, -25), (-50, -50), (-25, -75))
        prev = collections.defaultdict(float)
        prev[(n, n)] = 1.0
        curr =  collections.defaultdict(float)
        keep_going = True
        while keep_going:
            keep_going = False
            for (a, b), p in prev.items():
                if a > 0 and b > 0:
                    for da, db in ops:
                        a0 = max(0, a + da)
                        b0 = max(0, b + db)
                        if a0 and b0:
                            keep_going = True
                        curr[(a0, b0)] += (0.25 * p)
                else:
                    curr[(a, b)] += p
            prev, curr = curr, collections.defaultdict(float)

        return (
            sum(p for (a, b), p in prev.items() if a == 0 and b > 0) +
            prev[(0, 0)] * 0.5
        )


def test_1():
    n = 50
    expected = 0.62500
    assert abs(Solution().soupServings(n) - expected) <= EPS


def test_2():
    n = 100
    expected = 0.71875
    assert abs(Solution().soupServings(n) - expected) <= EPS