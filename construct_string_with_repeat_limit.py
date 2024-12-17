"""
LeetCode
2182. Construct String With Repeat Limit
December 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        CHAR, FREQ = 0, 1
        freqs = collections.Counter(s)
        queue = collections.deque(sorted(((k, v) for k, v in freqs.items()), reverse=True))
        soln = ['']
        while queue:
            a = queue.popleft()
            if soln[-1] == a[CHAR]:
                if queue:
                    b = queue.popleft()
                    soln.append(b[CHAR])
                    if b[FREQ] > 1:
                        b = (b[CHAR], b[FREQ]-1)
                        queue.appendleft(b)
                else:
                    break
            if a[FREQ] > repeatLimit:
                    soln.extend(a[CHAR] * repeatLimit)
                    a = (a[CHAR], a[FREQ] - repeatLimit)
                    queue.appendleft(a)
            else:
                soln.extend(a[CHAR] * a[FREQ])
        return ''.join(soln)
