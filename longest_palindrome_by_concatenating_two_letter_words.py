"""
LeetCode :: 2131. Longest Palindrome by Concatenating Two Letter Words
November 2022 Challenge
jramaswami
"""


from typing import *


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Count number of pairs: O(26^2)
        ord_a = ord('a')
        pair_matrix = [[0 for _ in range(26)] for _ in range(26)]
        for x, y in words:
            i = ord(x) - ord_a
            j = ord(y) - ord_a
            pair_matrix[i][j] += True

        # Count the number of left/right pairs and if there is *any* middle pair.
        # O(26^2)
        lr_prs = 0
        md_pr = 0
        for i in range(26):
            for j in range(i, 26):
                # Select the smallest number from ij and ji.  If the letters
                # are the same we will get the total number of pairs. If they
                # aren't the same we will get number of matching pairs.
                k = min(pair_matrix[i][j], pair_matrix[j][i])
                if k > 0:
                    if i == j:
                        # For two letter pairs, take matching two letter pairs
                        # as left/right.  We got total number of pairs so
                        # we must divide by 2.  Any odd two letter pair can go
                        # in the middle.  But only one middle pair is allowed.
                        lr, md = divmod(k, 2)
                    else:
                        # For different letter pairs, we take them as
                        # left/right.  We got the half the pairs, so that
                        # is the right number.
                        lr, md = k, 0
                    lr_prs += lr
                    md_pr = max(md_pr, md)

        # We now have the number of left/right pairs and if there is a middle
        # pair.  We must double the left/right pairs because they each have
        # a corresponding pair.  We then multiply by 2 because we need the
        # number of letters.
        return 2 * ((2 * lr_prs) + md_pr)



def test_1():
    words = ["lc","cl","gg"]
    expected = 6
    assert Solution().longestPalindrome(words) == expected


def test_2():
    words = ["ab","ty","yt","lc","cl","ab"]
    expected = 8
    assert Solution().longestPalindrome(words) == expected


def test_3():
    words = ["cc","ll","xx"]
    expected = 2
    assert Solution().longestPalindrome(words) == expected


def test_4():
    "WA"
    words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    expected = 22
    assert Solution().longestPalindrome(words) == expected