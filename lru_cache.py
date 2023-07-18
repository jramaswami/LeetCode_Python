"""
LeetCode
145. LRU Cache
July 2023 Challenge
jramaswami
"""


import heapq


class LRUCache:

    def __init__(self, capacity: int):
        self.lru_keys = []
        self.lru_time = dict()
        self.lru_values = dict()
        self.capacity = capacity
        self.time = 0

    def _use(self, key):
        self.lru_time[key] = self.time
        heapq.heappush(self.lru_keys, (self.time, key))
        self.time += 1

    def get(self, key: int) -> int:
        if key in self.lru_values:
            self._use(key)
            return self.lru_values[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.lru_values[key] = value
        self._use(key)
        while len(self.lru_values) > self.capacity:
            t, k = heapq.heappop(self.lru_keys)
            if t == self.lru_time[k]:
                del self.lru_values[k]
                del self.lru_time[k]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


null = None


def test_1():
    methods = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected = [null, null, null, 1, null, -1, null, -1, 3, 4]
    cache = LRUCache(*arguments[0])
    for (m, a, e) in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(cache, m)(*a)
        print(f"method={m} args={a} {e} {r}")
        assert e == r