"""
LeetCode
1701. Average Waiting Time
July 2024 Challenge
jramaswami
"""


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        available = 0
        total_wait_time = 0
        for arrival, cook_time in customers:
            start_time = max(available, arrival)
            end_time = start_time + cook_time
            wait_time = end_time - arrival
            total_wait_time += wait_time
            available = end_time
        return total_wait_time / len(customers)
