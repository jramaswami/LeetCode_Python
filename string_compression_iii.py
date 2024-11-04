"""
LeetCode
3163. String Compression III
November 2024 Challenge
jramawami
"""


class Solution:
    def compressedString(self, word: str) -> str:
        prev = ''
        freq = 0
        stack = []
        for curr in word:
            if not prev:
                prev = curr
                freq = 1
            elif freq == 9:
                stack.append(str(freq))
                stack.append(prev)
                prev = curr
                freq = 1
            elif prev != curr:
                stack.append(str(freq))
                stack.append(prev)
                prev = curr
                freq = 1
            else:
                freq += 1
        stack.append(str(freq))
        stack.append(prev)
        return ''.join(stack)
