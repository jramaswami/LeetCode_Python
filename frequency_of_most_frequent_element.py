"""
LeetCode
1838. Frequency of the Most Frequent Element
November 2023 Challenge
jramaswami
"""


import collections


class Solution:
    def maxFrequency(self, nums: List[int], max_cost: int) -> int:
        nums.sort()
        window = collections.deque()
        window_sum = 0
        soln = 0
        for n in nums:
            # Make all numbers in window equal to n
            window.append(n)
            window_sum += n

            while (n * len(window)) - window_sum > max_cost:
                window_sum -= window[0]
                window.popleft()
            soln = max(soln, len(window))
        return soln