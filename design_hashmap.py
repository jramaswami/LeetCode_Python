"""
LeetCode :: April 2022 Challenge :: 706. Design Hash Map
"""


class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v


class MyHashMap:

    def __init__(self):
        self.M = 99991
        self.buckets = [[] for _ in range(self.M)]

    def _find(self, key: int) -> tuple[int, int]:
        bid = key % self.M
        i = 0
        bucket = self.buckets[bid]
        while i < len(bucket):
            if bucket[i].key == key:
                return bid, i
        return bid, i

    def put(self, key: int, value: int) -> None:
        bid, i = self._find(key)
        if i >= len(self.buckets[bid]):
            self.buckets[bid].append(Entry(key, value))
        else:
            self.buckets[bid][i].value = value

    def get(self, key: int) -> int:
        bid, i = self._find(key)
        if i >= len(self.buckets[bid]):
            return -1
        return self.buckets[bid][i].value

    def remove(self, key: int) -> None:
        bid, i = self._find(key)
        if i < len(self.buckets[bid]):
            self.buckets[bid][i], self.buckets[bid][-1] = self.buckets[bid][-1], self.buckets[bid][i]
            self.buckets[bid].pop()
