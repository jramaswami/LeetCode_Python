"""
LeetCode :: November 2021 Challenge :: 668. Kth Smallest Number in Multiplication Table
jramaswami
"""


class Solution:

    def findKthNumber(self, height, width, k):
        """
        Binary search for the answer.
        """
        # The maximum value possible is height * width.
        lo = 0
        hi = height * width
        # k -= 1
        soln = 0
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            # Count the number of values less than mid and equal to mid.
            lt = 0
            eq = 0
            for n in range(1, height + 1):
                if mid % n == 0 and n * width >= mid:
                    # If mid is present in the row, then subtract one from
                    # lt and add one to eq.
                    lt += min(width, (mid // n) - 1)
                    eq += 1
                else:
                    # The number if elements in the row less than mid is
                    # the minimum of width and mid // n.
                    lt += min(width, mid // n)

            if lt < k:
                if lt + eq >= k:
                    return mid
                lo = mid + 1
            else:
                hi = mid - 1


#
#   Testing
#

import random


def brute_force(height, width, k):
    A = sorted(n * m for n in range(1, height + 1) for m in range(1, width + 1))
    print(A)
    return A[k-1]


def test_b1():
    height, width, k = 3, 3, 5
    expected = 3
    assert brute_force(height, width, k) == expected


def test_b2():
    height, width, k = 2, 3, 6
    expected = 6
    assert brute_force(height, width, k) == expected

def test_1():
    height, width, k = 3, 3, 5
    expected = 3
    assert Solution().findKthNumber(height, width, k) == expected


def test_2():
    height, width, k = 2, 3, 6
    expected = 6
    assert Solution().findKthNumber(height, width, k) == expected


def test_random():
    for _ in range(100):
        height, width = random.randint(1, 1000), random.randint(1, 1000)
        k = random.randint(1, height * width)
        assert Solution().findKthNumber(height, width, k) == brute_force(height, width, k)