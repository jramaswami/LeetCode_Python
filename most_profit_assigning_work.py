"""
LeetCode
826. Most Profit Assigning Work
June 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse=True)
        jobs = [(p, d) for p, d in zip(profit, difficulty)]
        jobs.sort(reverse=True)
        soln = i = j = 0
        while i < len(worker) and j < len(jobs):
            if worker[i] >= jobs[j][1]:
                soln += jobs[j][0]
                i += 1
            else:
                j += 1
        return soln
