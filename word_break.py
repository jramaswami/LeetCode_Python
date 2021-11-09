"""
LeetCode :: 139. Word Break
jramaswami
"""


class Solution:

    def wordBreak(self, s, word_dict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s) + 1):
            if dp[i]:
                for word in word_dict:
                    k = len(word)
                    if s[i:i+k] == word:
                        dp[i+k] = True
        return dp[-1]


def test_1():
    s = "leetcode"
    word_dict = ["leet","code"]
    assert Solution().wordBreak(s, word_dict) == True


def test_2():
    s = "applepenapple"
    word_dict = ["apple","pen"]
    assert Solution().wordBreak(s, word_dict) == True


def test_3():
    s = "catsandog"
    word_dict = ["cats","dog","sand","and","cat"]
    assert Solution().wordBreak(s, word_dict) == False