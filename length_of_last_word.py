"""
LeetCode
58. Length of Last Word
jramaswami
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        started_word = False
        word_length = 0
        for c in reversed(s):
            if c.isspace():
                if started_word:
                    return word_length
            else:
                started_word = True
                word_length += 1
        return word_length


def test_1():
    s = "Hello World"
    expected = 5
    assert Solution().lengthOfLastWord(s) == expected


def test_2():
    s = "   fly me   to   the moon  "
    expected = 4
    assert Solution().lengthOfLastWord(s) == expected


def test_3():
    s = "luffy is still joyboy"
    expected = 6
    assert Solution().lengthOfLastWord(s) == expected


def test_4():
    s = "abcde"
    expected = 5
    assert Solution().lengthOfLastWord(s) == expected