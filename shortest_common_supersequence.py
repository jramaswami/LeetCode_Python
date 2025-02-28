"""
LeetCode
1092. Shortest Common Supersequence
February 2025 Challenge
jramaswami

Thank You NeetCode.IO!
"""


import functools


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)

        prev = [str2[j:] for j in range(M)]
        prev.append('')
        
        for i in reversed(range(N)):
            curr = ['' for _ in range(M)]
            curr.append(str1[i:])
            for j in reversed(range(M)):
                if str1[i] == str2[j]:
                    curr[j] = str1[i] + prev[j+1]
                else:
                    a = str1[i] + prev[j]
                    b = str2[j] + curr[j+1]
                    if len(a) < len(b):
                        curr[j] = a
                    else:
                        curr[j] = b
            prev = curr
        
        return curr[0]
