"""
LeetCode :: June 2021 Challenge :: My Calendar I
jramaswami
"""


class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        """Return True if booking is accepted."""
        for start0, end0 in self.bookings:
            if max(start, start0) < min(end, end0):
                return False
        self.bookings.append((start, end))
        return True


def test_1():
    cal = MyCalendar()
    assert cal.book(10, 20)
    assert cal.book(15, 25) == False
    assert cal.book(20, 30)
    assert cal.book(30, 40)
    assert cal.book(0, 10)
