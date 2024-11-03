"""
LeetCode
796. Rotate String
November 2024 Challenge
jramaswami
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        def are_equal(i):
            g = 0
            while g < len(goal):
                if s[i] != goal[g]:
                    return False
                g += 1
                i = (i + 1) % len(goal)
            return True
        
        return (
            len(s) == len(goal) and 
            any(are_equal(i) for i, _ in enumerate(s))
        )
