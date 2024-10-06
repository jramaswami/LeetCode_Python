"""
LeetCode
1813. Sentence Similarity III
October 2024
jramaswmai
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words2) > len(words1):
            words1, words2 = words2, words1
        required_words = len(words1) - len(words2)

        if required_words == 0:
            return sentence1 == sentence2

        j = 0
        i = 0
        while i < len(words1):
            if j >= len(words2):
                if i == j:
                    # We have not subbed yet
                    # We can sub at the end
                    return True
                return False
            w1 = words1[i]
            w2 = words2[j]
            if w1 != w2:
                if i == j:
                    # Substitute skip forward
                    i += required_words
                else:
                    # Second time that words did not match
                    return False
            else:
                i += 1
                j += 1
        return True
