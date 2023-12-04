"""
LeetCode
2264. Largest 3-Same-Digit Number in String
December 2023 Challenge
jramaswami
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        soln = -1
        soln_str = ""
        for i, _ in enumerate(num[:-2]):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                n = int(num[i:i+3])
                if n > soln:
                    soln, soln_str = n, num[i:i+3]
        return soln_str