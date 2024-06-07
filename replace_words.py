"""
LeetCode
648. Replace Words
June 2024 Challenge
jramaswami
"""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda t: len(t))
        sentence_words = sentence.split()
        for dwd in dictionary:
            for i, swd in enumerate(sentence_words):
                if len(dwd) <= len(swd) and swd.startswith(dwd):
                    sentence_words[i] = dwd
        return " ".join(sentence_words)
