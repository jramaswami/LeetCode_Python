"""
LeetCode :: September 2022 Challenge :: 557. Reverse Words in a String III
jramaswami
"""


class Solution:

    def reverseWords(self, s: str) -> str:
        return " ".join("".join(reversed(t)) for t in s.split())



def test_1():
    s = "Let's take LeetCode contest"
    expected = "s'teL ekat edoCteeL tsetnoc"
    assert Solution().reverseWords(s) == expected


def test_2():
    s = "God Ding"
    expected = "doG gniD"
    assert Solution().reverseWords(s) == expected