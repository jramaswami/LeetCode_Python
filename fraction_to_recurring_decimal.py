"""
LeetCode
166. Fraction to Recurring Decimal
September 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        negative = False
        if numerator < 0 and denominator < 0:
            pass
        elif numerator < 0 or denominator < 0:
            negative = True

        numerator = abs(numerator)
        denominator = abs(denominator)
        
        digits = []
        p, q = divmod(numerator, denominator)
        digits.append(str(p))
        
        visited = dict()
        repeat = -1
        i = 1
        while q:
            if q in visited:
                repeat = visited[q]
                break
            visited[q] = i
            q *= 10
            p, q = divmod(q, denominator)
            digits.append(str(p))
            i += 1
        
        soln = []
        if negative:
            soln.append('-')
        for i, digit in enumerate(digits):
            if i == 1:
                soln.append('.')
            if i == repeat:
                soln.append('(')
            soln.append(digit)

        if repeat > 0:
            soln.append(')')
        
        return ''.join(soln)
