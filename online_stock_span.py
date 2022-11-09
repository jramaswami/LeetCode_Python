"""
LeetCode :: 901. Online Stock Span
November 2022 Challenge
jramaswami

Thank You Larry!
"""


import collections


SItem = collections.namedtuple('SItem', ['value', 'count'])


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1].value <= price:
            count += self.stack[-1].count
            self.stack.pop()
        self.stack.append(SItem(price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


null = None


def test_1():
    methods = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    args = [[], [100], [80], [60], [70], [60], [75], [85]]
    expected = [null, 1, 1, 1, 2, 1, 4, 6]
    spanner = StockSpanner()
    for m, a, e in zip(methods[1:], args[1:], expected[1:]):
        r = getattr(spanner, m)(*a)
        assert r == e