"""
LeetCode
1371. Find the Longest Substring Containing Vowels in Even Counts
September 2024 Challenge
jramaswami
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        curr = 0
        prefix = dict()
        # We have seen no vowels before starting
        prefix[0] = -1
        soln = 0
        for i, c in enumerate(s):
            # If this is a vowel update the current bitmask of vowel parity
            if c in 'aeiou':
                mask = 1 << (ord(c) - ord('a'))
                curr = curr ^ mask
            # If we have seen this bitmask before, we can remove the length
            # of the previous bitmask. If we haven't seen the bitmask before,
            # we have now.
            if curr in prefix:
                soln = max(soln, (i - prefix[curr]))
            else:
                prefix[curr] = i
        return soln
