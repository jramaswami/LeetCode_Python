"""
LeetCode :: April 2022 Challenge :: Peeking Iterator
jramaswami
"""


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        """
        self.iterator = iterator
        self.peeked = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        if self.peeked is None:
            self.peeked = self.iterator.next()
        return self.peeked

    def next(self):
        if self.peeked is None:
            return self.iterator.next()
        else:
            x = self.peeked
            self.peeked = None
            return x

    def hasNext(self):
        return self.peeked is not None or self.iterator.hasNext()
