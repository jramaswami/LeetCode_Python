"""
LeetCode :: June 2021 Challenge :: Candy
jramaswami
"""


class Solution:
    def candy(self, ratings):
        # Overall solution is O(n log n) time complexity with O(n) extra space.

        # Sort by ratings, keeping the index with the rating.
        # O(n log n)
        ratings0 = sorted((r, i) for i, r in enumerate(ratings))
        soln = [1 for _ in ratings]

        # For each rating, increase the amount of candy to be one more
        # than the largest candy of the ratings to the left and right
        # that are less than the current rating.  Because we do them in
        # order, we will only increase the candy if necessary.
        # O(n)
        for _, i in ratings0:
            min_value = 1
            if i > 0:
                if ratings[i-1] < ratings[i]:
                    min_value = max(min_value, soln[i-1] + 1)
            if i + 1 < len(ratings):
                if ratings[i+1] < ratings[i]:
                    min_value = max(min_value, soln[i+1] + 1)
            soln[i] = min_value

        # Compute the total amount of candy.
        # O(n)
        return sum(soln)


def test_1():
    ratings = [1,0,2]
    expected = 5
    assert Solution().candy(ratings) == expected


def test_2():
    ratings = [1,2,2]
    expected = 4
    assert Solution().candy(ratings) == expected


def test_3():
    """WA"""
    ratings = [29,51,87,87,72,12]
    expected = 12
    assert Solution().candy(ratings) == expected
