"""
LeetCode
1942. The Number of the Smallest Unoccupied Chair
October 2024 Challenge
jramaswami
"""


import heapq
import operator


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        last_chair = 0
        unoccupied_chairs = []
        occupied_chairs = []
        for i, t in enumerate(times):
            t.append(i)
        times.sort()
        for arrive, leave, i in times:
            # Handle anyone who leaves before current person arrives
            while occupied_chairs and occupied_chairs[0][0] <= arrive:
                _, chair = heapq.heappop(occupied_chairs)
                heapq.heappush(unoccupied_chairs, chair)
            
            if unoccupied_chairs:
                chair = heapq.heappop(unoccupied_chairs)
            else:
                chair = last_chair
                last_chair += 1
            heapq.heappush(occupied_chairs, (leave, chair))
            if i == targetFriend:
                return chair
