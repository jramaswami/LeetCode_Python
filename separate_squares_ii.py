"""
LeetCode
3454. Separate Squares II
January 2026 Challenge
jramaswami

REF: https://dev.to/om_shree_0709/beginner-friendly-guide-separate-squares-ii-leetcode-3454-c-python-javascript-1pp9
"""



from typing import List
from bisect import bisect_left


class SegmentTree:
    def __init__(self, x_coords):
        self.coords = x_coords
        self.n = len(x_coords)
        self.count = [0] * (4 * self.n)
        self.total_len = [0] * (4 * self.n)

    def update(self, node, start, end, L, R, val):
        if L <= start and end <= R:
            self.count[node] += val
        else:
            mid = (start + end) // 2
            if L <= mid:
                self.update(2 * node, start, mid, L, R, val)
            if R > mid:
                self.update(2 * node + 1, mid + 1, end, L, R, val)

        if self.count[node] > 0:
            self.total_len[node] = self.coords[end+1] - self.coords[start]
        elif start != end:
            self.total_len[node] = self.total_len[2 * node] + self.total_len[2 * node + 1]
        else:
            self.total_len[node] = 0

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        x_coords = sorted(list(set([s[0] for s in squares] + [s[0] + s[2] for s in squares])))
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + 1))
            events.append((y + 1, -1, x, x + 1))
        events.sort()

        st = SegmentTree(x_coords)
        states = []
        total_area = 0
        for i in range(len(events) - 1):
            L = bisect_left(x_coords, events[i][2])
            R = bisect_left(x_coords, events[i][3]) - 1
            st.update(1, 0, len(x_coords) - 2, L, R, events[i][1])

            height = events[i+1][0] - events[i][0]
            width = st.total_len[1]
            total_area += height * width
            states.append((events[i][0], width, events[i+1][0]))

        half_area = total_area / 2.0
        current_area = 0
        for y_start, width, y_end in states:
            stage_area = (y_end - y_start) * width
            if current_area + stage_area >= half_area - 1e9:
                if width == 0: return y_start
                return y_start + (half_area - current_area) / width
            current_area += stage_area
        return events[-1][0]



EPS = pow(10, -5)


def test_1():
    squares = [[0,0,1],[2,2,1]]
    expected = 1.0000
    result = Solution().separateSquares(squares)
    assert abs(expected - result) < EPS