"""
LeetCode
3606. Coupon Code Validator
December 2025 Challenge
jramaswami
"""


import string
from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def valid_char(c):
            if c in string.ascii_letters:
                return True
            if c in string.digits:
                return True
            return c == '_'

        def valid_coupon(cd, bl, ac):
            if not ac:
                return False
            if bl not in ("electronics", "grocery", "pharmacy", "restaurant"):
                return False
            return cd and all(valid_char(c) for c in cd)

        soln = []
        for cd, bl, ac in zip(code, businessLine, isActive):
            if valid_coupon(cd, bl, ac):
                soln.append((bl, cd))
        soln.sort()
        return [t[1] for t in soln]