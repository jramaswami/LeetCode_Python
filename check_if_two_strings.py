"""
LeetCode :: 1662. Check If Two String Arrays are Equivalent
jramaswami

Of course, the easy way would be to join the arrays together into a string
and test for equality.  But, where is the fun in that!
"""
from typing import *


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_len = sum(len(w) for w in word1)
        word2_len = sum(len(w) for w in word2)
        # To be equal they must be the same length.
        if word1_len != word2_len:
            return False
        
        word1_word_index = word2_word_index = 0
        word1_char_index = word2_char_index = 0
        while word1_word_index < len(word1):
            if word1[word1_word_index][word1_char_index] != word2[word2_word_index][word2_char_index]:
                return False

            word1_char_index += 1
            if word1_char_index >= len(word1[word1_word_index]):
                    word1_word_index += 1
                    word1_char_index = 0

            word2_char_index += 1
            if word2_char_index >= len(word2[word2_word_index]):
                    word2_word_index += 1
                    word2_char_index = 0

        return True

def test_1():
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    assert Solution().arrayStringsAreEqual(word1, word2) == True

def test_2():
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    assert Solution().arrayStringsAreEqual(word1, word2) == False


def test_3():
    word1  = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    assert Solution().arrayStringsAreEqual(word1, word2) == True
