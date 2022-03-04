"""
LeetCode :: March 2022 Challenge :: 799. Champagne Tower
jramaswami
"""


def S(n):
    "Return sum of [1 .. n]."""
    return (n * (n+1)) // 2

class Solution:

    def champagneTower(self, poured, query_row, query_glass):
        # Move indices to one based.
        query_row += 1
        query_glass += 1
        # Given query_row there are 1+2+3+...+query_row-1 cups
        # above it.
        cups_above = S(query_row-1)
        cups_including = cups_above + query_row
        if poured <= cups_above:
            # Did not pour enough to reach query row.
            return 0.0
        if poured >= cups_including:
            # Pour enough to fill query row.
            return 1.0
        # There are n glasses.  All but the first and last glasses have two
        # glasses from above pouring into them.  We can compute the ratio
        # of how much of each pour the glasses in this row will get.
        denominator = (2 * query_row) - 2
        numerator = 2 * (poured - cups_above)
        if query_glass == 1 or query_glass == query_row:
            numerator = (poured - cups_above)
        return numerator / denominator



def test_1():
    poured = 1
    query_row = 1
    query_glass = 1
    expected = 0.00000
    assert Solution().champagneTower(poured, query_row, query_glass) == expected


def test_2():
    poured = 2
    query_row = 1
    query_glass = 1
    expected = 0.50000
    assert Solution().champagneTower(poured, query_row, query_glass) == expected


def test_3():
    poured = 100000009
    query_row = 33
    query_glass = 17
    expected = 1.00000
    assert Solution().champagneTower(poured, query_row, query_glass) == expected


def test_4():
    "WA"
    poured = 25
    query_row =  6
    query_glass = 1
    expected = 0.18750
    assert Solution().champagneTower(poured, query_row, query_glass) == expected
