"""
LeetCode :: June 2021 Challenge :: My Calendar I
jramaswami
"""

def overlaps(a, b, x, y):
    # a------b
    #     x------y
    #
    # a--------------b
    #      x-----y
    if a <= x < b:
        return True

    #     a-------b
    # x------y
    #
    #      a-----b
    # x--------------y
    if x <= a < y:
        return True

    return False

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        """Return True if booking is accepted."""
        before = []
        after = []
        for start0, end0 in self.bookings:
            # Overlapping bookings!
            if overlaps(start0, end0, start, end):
                return False

            # Booking that ends before new booking.
            if end0 <= start:
                before.append((start0, end0))

            # Booking that starts after new booking.
            if end <= start0:
                after.append((start0, end0))

        before.append((start, end))
        before.extend(after)
        self.bookings = before
        return True


def test_1():
    cal = MyCalendar()
    assert cal.book(10, 20)
    assert cal.book(15, 25) == False
    assert cal.book(20, 30)
    assert cal.book(30, 40)
    assert cal.book(0, 10)
