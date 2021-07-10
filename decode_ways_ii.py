"""
LeetCode :: July 2021 Challenge :: Decode Ways II
jramaswami
"""


class Solution():
    def numDecodings(self, S):
        MOD = pow(10, 9) + 7
        dp = [0 for _ in range(len(S)+1)]
        dp[0] = 1
        # Convert to digits for convenience, '*' -> -1
        S0 = [-1 if c == '*' else int(c) for c in S]

        # Left to right.
        for i, c in enumerate(S0):
            # Single digit i, excludes 0 by itself.
            if c < 0:
                dp[i+1] = (dp[i+1] + ((9 * dp[i]) % MOD)) % MOD
            elif c > 0:
                dp[i+1] = (dp[i+1] + dp[i]) % MOD

            # Double digit. (i, i+1)
            if i + 1 < len(S0):
                if c == 1:
                    if S0[i+1] >= 0:
                        # 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
                        dp[i+2] = (dp[i+2] + dp[i]) % MOD
                    else:
                        # 1* (9 possibilities, excludes 10)
                        dp[i+2] = (dp[i+2] + ((9 * dp[i]) % MOD)) % MOD
                elif c == 2:
                    if 0 <= S0[i+1] <= 6:
                        # 20, 21, 22, 23, 24, 25, 26
                        dp[i+2] = (dp[i+2] + dp[i]) % MOD
                    elif S0[i+1] < 0:
                        # 2* (6 Possibilities, excludes 20)
                        dp[i+2] = (dp[i+2] + ((6 * dp[i]) % MOD)) % MOD
                elif c == -1:
                    if 0 <= S0[i+1] <= 6:
                        # *0, *1, *2, *3, *4, *5, *6 then * can be 1 or 2
                        dp[i+2] = (dp[i+2] + ((2* dp[i]) % MOD)) % MOD
                    elif S0[i+1] > 6:
                        # *7, *8, *9 then * must be 1
                        dp[i+2] = (dp[i+2] + dp[i]) % MOD
                    elif S0[i+1] < 0:
                        # **
                        # 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24,
                        # 25, 26
                        # 15 possibilities (excludes 10 and 20).
                        dp[i+2] = (dp[i+2] + ((15 * dp[i]) % MOD)) % MOD
        return dp[-1] % MOD


def test_1():
    s = "*"
    expected = 9
    assert Solution().numDecodings(s) == expected


def test_2():
    s = "1*"
    expected = 18
    assert Solution().numDecodings(s) == expected


def test_3():
    s = "2*"
    expected = 15
    assert Solution().numDecodings(s) == expected


def test_4():
    s = "*29"
    # [1, 9, 2+9, 0+2+9] == 11
    expected = 11
    assert Solution().numDecodings(s) == expected
