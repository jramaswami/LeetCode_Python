"""
LeetCode
1845. Seat Reservation Manager
November 2023 Challenge
jramaswami
"""


import heapq


class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n+1))
        heapq.heapify(self.heap)

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)