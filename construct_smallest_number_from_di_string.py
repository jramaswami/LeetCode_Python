"""
LeetCode
2375. Construct Smallest Number From DI String
February 2025 Challenge
jramaswami
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        soln = '9' * (len(pattern) + 1)
        def rec(i, acc):
            if i >= len(pattern):
                t = ''.join(str(n) for n in acc)
                nonlocal soln
                soln = min(soln, t)
            else:
                if pattern[i] == 'I':
                    for n in range(acc[-1]+1, 10):
                        if n not in acc:
                            acc.append(n)
                            rec(i+1, acc)
                            acc.pop()
                else:
                    for n in range(1, acc[-1]):
                        if n not in acc:
                            acc.append(n)
                            rec(i+1, acc)
                            acc.pop()
        
        for n in range(1, 10):
            rec(0, [n, ])
        return  soln
