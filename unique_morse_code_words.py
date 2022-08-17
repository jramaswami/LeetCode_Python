"""
LeetCode :: August 2022 Challenge :: 804. Unique Morse Code Words
jramaswami
"""


from typing import *


MORSE = [
    ".-","-...","-.-.","-..",".","..-.","--.","....","..",
    ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
    "...","-","..-","...-",".--","-..-","-.--","--.."
]


class Solution:

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set("".join(MORSE[ord(c) - ord('a')] for c in w) for w in words))


def test_1():
    words = ["gin","zen","gig","msg"]
    expected = 2
    assert Solution().uniqueMorseRepresentations(words) == expected


def test_2():
    words = ["a"]
    expected = 1
    assert Solution().uniqueMorseRepresentations(words) == expected