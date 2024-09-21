"""
LeetCode
386. Lexicographical Numbers
September 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        def rec(x, n, soln):
            if x > n:
                return

            soln.append(x)
            for t in range(10):
                x0 = (10 * x) + t
                rec(x0, n, soln)

        soln = []
        for x in range(1,10):
            rec(x, n, soln)
        return soln


def test_1():
    n = 13
    output = [1,10,11,12,13,2,3,4,5,6,7,8,9]
    assert Solution().lexicalOrder(n) == output
