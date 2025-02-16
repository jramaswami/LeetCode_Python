"""
LeetCode
1718. Construct the Lexicographically Largest Valid Sequence
February 2025 Challenge
jramaswami

Thank You NeetCode.IO!
"""


from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = (2 * n) - 1
        soln = [0 for _ in range(length)]
        used = set()

        def rec(i):
            if i >= len(soln):
                return True
            for x in reversed(range(1, n+1)):
                if x in used:
                    continue
                if x > 1 and (i+x >= len(soln) or soln[i+x]):
                    continue
                used.add(x)
                soln[i] = x
                if x > 1:
                    soln[i+x] = x
                j = i + 1
                while j < len(soln) and soln[j]:
                    j += 1
                if rec(j):
                    return True
                used.remove(x)
                soln[i] = 0
                if x > 1:
                    soln[i+x] = 0
            return False
        rec(0)
        return soln
