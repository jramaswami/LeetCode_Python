"""
LeetCode :: August 2021 Challenge :: Rectangle Area II
jramaswami
"""

MOD = pow(10, 9) + 7


def is_active(rectangle, x):
    """Return True if rectangle is active at given x."""
    return rectangle[0] <= x <= rectangle[2]


def merge_intervals(rectangles):
    """Return list of y intervals that occur at x."""
    intervals = []
    curr_start = rectangles[0][1]
    curr_end = rectangles[0][3]
    for r in rectangles:
        if curr_start <= r[1] <= curr_end:
            curr_end = max(curr_end, r[3])
        else:
            intervals.append((curr_start, curr_end))
            curr_start, curr_end = r[1], r[3]
    intervals.append((curr_start, curr_end))
    return intervals


class Solution:
    def rectangleArea(self, rectangles):
        # Sort the rectangles by y values.
        rectangles.sort(key=lambda r: (r[1], r[3]))
        print(rectangles)

        # Create events along x-axis
        event_set = set()
        for x1, _, x2, _ in rectangles:
            event_set.add(x1)
            event_set.add(x2)

        total_area = 0
        events = sorted(event_set)
        for a, b in zip(events[:-1], events[1:]):
            active_rectangles = [r for r in rectangles if is_active(r, a) and is_active(r, b)]
            intervals = merge_intervals(active_rectangles)
            for l, r in intervals:
                total_area += (r - l) * (b - a)

        return total_area % MOD



def test_1():
    rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    expected = 6
    assert Solution().rectangleArea(rectangles) == expected


def test_2():
    rectangles = [[0,0,1000000000,1000000000]]
    expected = 49
    assert Solution().rectangleArea(rectangles) == expected


def test_3():
    rectangles = [[0,0,1,1],[2,2,3,3]]
    expected = 49
    assert Solution().rectangleArea(rectangles) == expected
