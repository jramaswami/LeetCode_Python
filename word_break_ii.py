"""
LeetCode
140. Word Break II
May 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        soln = []
        words = set(wordDict)
        def rec(i, j, acc):
            if i == len(s):
                soln.append(" ".join(acc))
                return
            if j >= len(s):
                return

            if s[i:j+1] in words:
                acc.append(s[i:j+1])
                rec(j+1, j+1, acc)
                acc.pop()
            rec(i, j+1, acc)

        rec(0, 0, [])
        return soln


def test_1():
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    expected = ["cats and dog","cat sand dog"]
    result = Solution().wordBreak(s, wordDict)
    assert set(result) == set(expected)


def test_2():
    s = "pineapplepenapple"
    wordDict = ["apple","pen","applepen","pine","pineapple"]
    expected = ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
    result = Solution().wordBreak(s, wordDict)
    print(result)
    assert set(result) == set(expected)



def test_3():
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    expected = []
    result = Solution().wordBreak(s, wordDict)
    assert set(result) == set(expected)
