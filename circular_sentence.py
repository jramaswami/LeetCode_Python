"""
LeetCode
2490. Circular Sentence
November 2024 Challenge
jramaswami
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        prev = sentence[-1]
        for word in sentence.split():
            curr = word[0]
            if curr != prev:
                return False
            prev = word[-1]
        return True
