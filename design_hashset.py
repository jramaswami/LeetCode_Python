"""
LeetCode :: April 2022 Challenge :: 705. Design HashSet
jramaswami
"""


class MyHashSet:

    def __init__(self):
        self.M = 15013
        self.A = [[] for _ in range(self.M)]

    def add(self, key):
        slot = key % self.M
        if key not in self.A[slot]:
            self.A[slot].append(key)

    def remove(self, key):
        slot = key % self.M
        try:
            i = self.A[slot].index(key)
            self.A[slot][i] = self.A[slot][-1]
            self.A[slot].pop()
        except:
            pass

    def contains(self, key):
        slot = key % self.M
        return key in self.A[slot]



#
# Testing
#


null = None
true = True
false = False


def test_1():
    methods = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    arguments = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    expected = [null, null, null, true, false, null, true, null, false]
    hs = MyHashSet()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(hs, m)(*a) == e


def test_2():
    "RTE"
    methods = ["MyHashSet","add","remove","add","remove","remove","add","add","add","add","remove"]
    arguments = [[],[9],[19],[14],[19],[9],[0],[3],[4],[0],[9]]
    expected = [null,null,null,null,null,null,null,null,null,null,null]
    hs = MyHashSet()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(hs, m)(*a) == e
