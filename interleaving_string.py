"""
LeetCode :: June 2021 Challenge :: Interleaving String
jramaswami
"""


from typing import *
from functools import lru_cache


def solve_recursively(s1, s2, s3):
    """Recursive solution."""

    @lru_cache(maxsize=None)
    def solve0(i1, i2):
        """Recursive helper function."""
        # If both indexes are at the end, then we have interleaved the string.
        if i1 >= len(s1) and i2 >= len(s2) and i1 + i2 >= len(s3):
            return True
        
        soln = False
        if i1 < len(s1) and i1 + i2 < len(s3) and s1[i1] == s3[i1 + i2]:
            soln = soln or solve0(i1 + 1, i2)
        if i2 < len(s2) and i1 + i2 < len(s3) and s2[i2] == s3[i2 + i1]:
            soln = soln or solve0(i1, i2 + 1)

        return soln

    return solve0(0, 0)



def solve_dfs(s1, s2, s3):
    """Solve using dfs."""
    visited = set()
    queue = [(0, 0)]
    while queue:
        i1, i2 = queue.pop()
        if i1 + i2 >= len(s3) and i1 >= len(s1) and i2 >= len(s2):
            return True
        
        if i1 < len(s1) and i1 + i2 < len(s3) and s1[i1] == s3[i1 + i2]:
            T = (i1 + 1, i2)
            if T not in visited:
                visited.add(T)
                queue.append(T)
        if i2 < len(s2) and i1 + i2 < len(s3) and s2[i2] == s3[i1 + i2]:
            T = (i1, i2 + 1)
            if T not in visited:
                visited.add(T)
                queue.append(T)

    return False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return solve_recursively(s1, s2, s3)


def test_1():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    assert Solution().isInterleave(s1, s2, s3) == True


def test_2():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    assert Solution().isInterleave(s1, s2, s3) == False


def test_3():
    s1 = ""
    s2 = ""
    s3 = ""
    assert Solution().isInterleave(s1, s2, s3) == True


def test_4():
    """WA"""
    s1 = ""
    s2 = ""
    s3 = "a"
    assert Solution().isInterleave(s1, s2, s3) == False


def test_5():
    """WA"""
    s1 = "a"
    s2 = "b"
    s3 = "a"
    assert Solution().isInterleave(s1, s2, s3) == False


def test_6():
    """TLE"""
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    assert Solution().isInterleave(s1, s2, s3) == False
