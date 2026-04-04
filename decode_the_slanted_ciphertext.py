"""
LeetCode
2075. Decode the Slanted Ciphertext
April 2026 Challenge
jramaswami
"""


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        curr_col = r = c = 0
        soln = []
        width = len(encodedText) // rows
        while curr_col < width:
            if r < rows and c < width:
                i = (r * width) + c
                soln.append(encodedText[i])
                r += 1
                c += 1
            else:
                r = 0
                curr_col += 1
                c = curr_col
        return (''.join(soln)).rstrip()