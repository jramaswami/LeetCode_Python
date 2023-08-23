"""
LeetCode
767. Reorganize String
August 2023
jramaswami
"""


import heapq
import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = collections.Counter(s)
        queue = [(-t, k) for k, t in freqs.items()]
        heapq.heapify(queue)
        soln = []
        while queue:
            freq_a, a = heapq.heappop(queue)
            soln.append(a)

            popped_b = False
            if queue:
                freq_b, b = heapq.heappop(queue)
                soln.append(b)
                popped_b = True

            if freq_a + 1 != 0:
                heapq.heappush(queue, (freq_a + 1, a))

            if popped_b and freq_b + 1 != 0:
                heapq.heappush(queue, (freq_b + 1, b))

        for i, _ in enumerate(soln[1:], start=1):
            if soln[i-1] == soln[i]:
                return ""
        return "".join(soln)