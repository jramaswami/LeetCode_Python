"""
LeetCode
2327. Number of People Aware of a Secret
September 2025 Challenge
jramaswami
"""


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = pow(10, 9) + 7
        knows = [0 for _ in range(n)]
        forgets = [0 for _ in range(n)]
        knows[0] = 1
        for day in range(n):
            for telling_day in range(day+delay, min(n, day+forget)):
                knows[telling_day] += knows[day]
            if day+forget < n:
                forgets[day+forget] += knows[day]
        print(knows, sum(knows))
        print(forgets, sum(forgets))
        return (sum(knows) - sum(forgets)) % MOD
        

def test_1():
    n = 6
    delay = 2
    forget = 4
    expected = 5
    assert Solution().peopleAwareOfSecret(n, delay, forget) == expected


def test_2():
    n = 4
    delay = 1
    forget = 3
    expected = 6
    assert Solution().peopleAwareOfSecret(n, delay, forget) == expected
