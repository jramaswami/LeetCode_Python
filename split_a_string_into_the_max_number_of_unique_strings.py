"""
LeetCode
1593. Split a String Into the Max Number of Unique Substrings
October 2024 Challenge
jramaswami
"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def rec(i, acc, prev):
            if i >= len(s):
                if acc not in prev:
                    return len(prev) + 1
                return 0
            
            # Break before here
            result = 0
            if acc and acc not in prev:
                prev.add(acc)
                result = max(result, rec(i+1, s[i], prev))
                prev.remove(acc)
            # Break after here
            t = acc+s[i]
            result = max(result, rec(i+1, t, prev))
            return result
        
        return rec(0, '', set())
