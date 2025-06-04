"""
LeetCode
3403. Find the Lexicographically Largest String From the Box I
June 2025 Challenge
jramaswami
"""


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word) - (numFriends - 1)
        soln = ""
        for i in range(len(word)):
            if soln < word[i:i+n]:
                soln = word[i:i+n]
        return soln