"""
LeetCode
1052. Grumpy Bookstore Owner
June 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfaction = sum(c for g, c in zip(grumpy, customers) if g == 0)
        soln = total_satisfaction
        current_delta = 0
        window = collections.deque()
        for g, c in zip(grumpy, customers):
            d = g * c
            current_delta += d
            window.append(d)
            if len(window) > minutes:
                current_delta -= window[0]
                window.popleft()
            
            if len(window) == minutes:
                soln = max(soln, total_satisfaction + current_delta)
        
        return soln
