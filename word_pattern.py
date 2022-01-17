"""
LeetCode :: January 2022 Challenge :: 290. Word Pattern
jramaswami
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        visited = dict()
        for p, w in zip(pattern, s.strip().split()):
            if p in visited:
                if w != visited[p]:
                    return False
            else:
                visited[p] = w
        return True



def test_1():
    pattern = "abba"
    s = "dog cat cat dog"
    assert Solution().wordPattern(pattern, s) == True


def test_2():
    pattern = "abba"
    s = "dog cat cat fish"
    assert Solution().wordPattern(pattern, s) == False


def test_3():
    pattern = "aaaa"
    s = "dog cat cat dog"
    assert Solution().wordPattern(pattern, s) == False


def test_4():
    "WA"
    pattern = "abba"
    s = "dog dog dog dog"
    assert Solution().wordPattern(pattern, s) == False
