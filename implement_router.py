"""
LeetCode
3508. Implement Router
September 2025 Challenge
jramaswami
"""


import collections
import dataclasses
from typing import List


@dataclasses.dataclass(frozen = True)
class Packet:
    source: int
    destination: int
    timestamp: int


class Router:

    def __init__(self, memory_limit: int):
        self.memory_limit = memory_limit
        self.packet_queue = collections.deque()
        self.packet_set = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = Packet(source, destination, timestamp)
        # A packet is considered a duplicate if another packet with the
        # same source, destination, and timestamp already exists in the router.
        if packet in self.packet_set:
            return False
        # If adding a new packet would exceed this limit, the oldest
        # packet must be removed to free up space.
        while len(self.packet_queue) >= self.memory_limit:
            x_packet = self.packet_queue.popleft()
            self.packet_set.remove(x_packet)
        self.packet_queue.append(packet)
        self.packet_set.add(packet)
        return True

    def forwardPacket(self) -> List[int]:
        if self.packet_queue:
            packet = self.packet_queue.popleft()
            self.packet_set.remove(packet)
            return [packet.source, packet.destination, packet.timestamp]
        return []

    def getCount(self, destination: int, start_time: int, end_time: int) -> int:
        count = 0
        for p in self.packet_set:
            if p.destination == destination and start_time <= p.timestamp <= end_time:
                count += 1
        return count

null = None
true = True
false = False

def test_1():
    fs = ["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket","forwardPacket", "addPacket", "getCount"]
    ps = [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]
    es = [null, true, true, false, true, true, [2, 5, 90], true, 1]
    R = Router(*ps[0])
    for f, p, e in zip(fs[1:], ps[1:], es[1:]):
        assert getattr(R, f)(*p) == e


def test_2():
    fs = ["Router", "addPacket", "forwardPacket", "forwardPacket"]
    ps = [[2], [7, 4, 90], [], []]
    es = [null, true, [7, 4, 90], []]
    R = Router(*ps[0])
    for f, p, e in zip(fs[1:], ps[1:], es[1:]):
        assert getattr(R, f)(*p) == e


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)