"""
LeetCode
145. LRU Cache
July 2023 Challenge
jramaswami
"""


import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, False)
        while len(self.cache) > self.capacity:
            self.cache.popitem(last=True)


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