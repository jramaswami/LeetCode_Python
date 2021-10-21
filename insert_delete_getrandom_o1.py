"""
LeetCode :: October 2021 Challlenge :: 380. Insert Delete GetRandom O(1)
jramaswami
"""


import random


class SetItem:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer

    def __repr__(self):
        return f"SetItem({self.value=}, {self.pointer=})"


class RandomizedSet:
    """
    Use separate chaining for hash table.
    Use a different array to allow for random selection of numbers.
    """

    def __init__(self):
        # There are at most 2 * 10 ^ 5 calls.  Add a random padding to
        # foil any attempt to cause all values to chain to the same key.
        self.M = (2 * pow(10, 5)) + random.randint(0, 100)
        self.table = [[] for _ in range(self.M)]
        self.numbers = []

    def insert(self, val: int) -> bool:
        key = val % self.M
        for item in self.table[key]:
            if item.value == val:
                return False
        item = SetItem(val, len(self.numbers))
        self.table[key].append(item)
        self.numbers.append(item)
        return True

    def _find(self, key, val):
        for index, item in enumerate(self.table[key]):
            if item.value == val:
                return index
        return -1

    def remove(self, val: int) -> bool:
        key = val % self.M
        index = self._find(key, val)
        if index >= 0:
            item = self.table[key][index]
            # Remove from table.
            self.table[key].pop(index)
            # Remove from numbers by swapping with last item in numbers
            # and then popping.
            self.numbers[item.pointer], self.numbers[-1] = self.numbers[-1], self.numbers[item.pointer]
            self.numbers[item.pointer].pointer = item.pointer
            self.numbers.pop()
            return True
        return False

    def getRandom(self) -> int:
        # Choose random index.
        index = random.randint(0, len(self.numbers) - 1)
        return self.numbers[index].value


def test_1():
    S = RandomizedSet()
    for n in range(10):
        S.insert(n)

    for n in range(9):
        S.remove(n)

    assert len(S.numbers) == 1
    assert S.numbers[0].value == 9


def test_2():
    S = RandomizedSet()
    assert S.insert(1) == True
    assert S.remove(2) == False
    assert S.insert(2) == True
    assert S.remove(1) == True
    assert S.insert(2) == False
    assert S.getRandom() == 2
