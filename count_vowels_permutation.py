"""
LeetCode :: August 2022 Challenge :: Count Vowels Permutation
jramaswami
"""


class Solution:
    def countVowelPermutation(self, n):
        A, E, I, O, U = range(5)
        MOD = pow(10, 9) + 7
        # dp[length][vowel]
        dp = [[0 for _ in range(5)] for _ in range(n+1)]
        dp[1] = [1 for _ in range(5)]
        for i in range(2, n+1):
            # a: Each vowel 'a' may only be followed by an 'e'.
            dp[i][E] = (dp[i][E] + dp[i-1][A]) % MOD
            # e: Each vowel 'e' may only be followed by an 'a' or an 'i'.
            dp[i][A] = (dp[i][A] + dp[i-1][E]) % MOD
            dp[i][I] = (dp[i][I] + dp[i-1][E]) % MOD
            # i: Each vowel 'i' may not be followed by another 'i'.
            dp[i][A] = (dp[i][A] + dp[i-1][I]) % MOD
            dp[i][E] = (dp[i][E] + dp[i-1][I]) % MOD
            dp[i][O] = (dp[i][O] + dp[i-1][I]) % MOD
            dp[i][U] = (dp[i][U] + dp[i-1][I]) % MOD
            # o: Each vowel 'o' may only be followed by an 'i' or a 'u'.
            dp[i][I] = (dp[i][I] + dp[i-1][O]) % MOD
            dp[i][U] = (dp[i][U] + dp[i-1][O]) % MOD
            # u: Each vowel 'u' may only be followed by an 'a'.
            dp[i][A] = (dp[i][A] + dp[i-1][U]) % MOD

        return sum(dp[-1]) % MOD


def test_1():
    assert Solution().countVowelPermutation(1) == 5


def test_2():
    assert Solution().countVowelPermutation(2) == 10


def test_3():
    assert Solution().countVowelPermutation(5) == 68
