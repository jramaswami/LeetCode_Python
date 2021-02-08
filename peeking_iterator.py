"""
LeetCode :: Peeking Iterator
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
        if self.peeked:
            v = self.peeked
            self.peeked = None
            return v
        else:
            return self.iterator.next()

    def hasNext(self):
        return self.iterator.hasNext() or self.peeked is not None
