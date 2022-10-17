"""
LeetCode :: October 2022 Challenge :: 1832. Check if the Sentence Is Pangram
jramaswami
"""


import string


class Solution:

    def checkIfPangram(self, sentence: str) -> bool:
        letters = {c: False for c in string.ascii_lowercase}
        for c in sentence:
            letters[c] = True
        return all(letters.values())


def test_1():
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    expected = True
    assert Solution().checkIfPangram(sentence) == expected


def test_2():
    sentence =sentence = "leetcode"
    expected = False
    assert Solution().checkIfPangram(sentence) == expected
