"""
LeetCode :: May 2022 Challenge :: Flatten Nested List Iterator
jramaswami
"""


class NestedIterator:
    def __init__(self, nested_list):
        self.stack = []
        if nested_list:
            self.stack = [(nested_list, 0)]

    def _shouldpop(self):
        if self.stack:
            if self.stack[-1][1] >= len(self.stack[-1][0]):
                return True

    def _fixstack(self):
        while self.stack and self.stack[-1][1] >= len(self.stack[-1][0]):
            self.stack.pop()

    def next(self):
        L, i = self.stack[-1]
        if isinstance(L[i], list):
            self.stack[-1] = (L, i+1)
            self.stack.append((L[i], 0))
            x = self.next()
        else:
            x = L[i]
            self.stack[-1] = (L, i+1)
        return x

    def hasNext(self):
        self._fixstack()
        return len(self.stack) > 0


def test_1():
    nested_list = [[1,1],2,[1,1]]
    expected = [1,1,2,1,1]
    iterator, result = NestedIterator(nested_list), []
    while iterator.hasNext():
        result.append(iterator.next())
    assert result == expected


def test_2():
    nested_list = [1,[4,[6]]]
    expected = [1,4,6]
    iterator, result = NestedIterator(nested_list), []
    while iterator.hasNext():
        result.append(iterator.next())
    assert result == expected


def test_3():
    nested_list = []
    expected = []
    iterator, result = NestedIterator(nested_list), []
    while iterator.hasNext():
        result.append(iterator.next())
    assert result == expected


def test_4():
    nested_list = [[]]
    expected = []
    iterator, result = NestedIterator(nested_list), []
    while iterator.hasNext():
        result.append(iterator.next())
    assert result == expected