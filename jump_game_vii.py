"""
LeetCode
1871. Jump Game VII
May 2026 Challenge
jramaswami
"""



class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        reachable = {0: -1}
        for i, x in enumerate(s):
            if x == '0' and i in reachable:
                left = i + minJump
                right = min(i + maxJump + 1, len(s))
                for j, y in enumerate(s[left:right], start=left):
                    if y == '0' and j not in reachable:
                        reachable[j] = i
        return len(s)-1 in reachable