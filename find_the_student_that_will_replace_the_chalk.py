"""
LeetCode
1894. Find the Student that Will Replace the Chalk
jramaswami
"""

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        x = 0
        while k:
            if k < chalk[x]:
                break
            k -= chalk[x]
            x += 1
        return x
