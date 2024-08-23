"""
LeetCode
592. Fraction Addition and Subtraction
August 2024 Challenge
jramaswami
"""


import fractions


class Solution:
    def fractionAddition(self, expression: str) -> str:
        terms = []
        stack = []
        for char in expression:
            if (char == '-' or char == '+') and stack:
                term = ''.join(stack)
                terms.append(fractions.Fraction(term))
                stack = []
            stack.append(char)
        term = ''.join(stack)
        terms.append(fractions.Fraction(term))
        soln = sum(terms)
        
        return f'{soln.numerator}/{soln.denominator}'
