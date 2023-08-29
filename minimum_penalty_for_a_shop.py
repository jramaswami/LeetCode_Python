"""
LeetCode
2483. Minimum Penalty for a Shop
August 2023 Challenge
jramaswami
"""


import itertools


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        INF = pow(10, 20)
        no_customers_prefix = list(itertools.accumulate((0 if t == 'Y' else 1 for t in customers)))
        customers_suffix = list(itertools.accumulate((1 if t == 'Y' else 0 for t in reversed(customers))))[::-1]

        print(f'{no_customers_prefix=}\n{customers_suffix=}')
        def get(arr, i):
            "Helper function to get value from array, but return zero when out of bounds"
            if i < 0 or i >= len(arr):
                return 0
            return arr[i]

        min_penalty = INF
        min_closing = INF
        for closing_before in range(len(customers)+1):
            penalty = 0
            # Penalized for all non-customer hours up to but not including
            # closing before
            closing_after = closing_before - 1
            penalty += get(no_customers_prefix, closing_after)
            # Penalized for all customer hours after closing before
            penalty += get(customers_suffix, closing_before)
            print(f'{closing_after=} {get(no_customers_prefix, closing_after)} {closing_before=} {get(customers_suffix, closing_before)} {penalty=}')
            if penalty < min_penalty:
                min_closing = closing_before
                min_penalty = penalty
        return min_closing


def test_1():
    customers = "YYNY"
    expected = 2
    assert Solution().bestClosingTime(customers) == expected


def test_2():
    customers = "NNNNN"
    expected = 0
    assert Solution().bestClosingTime(customers) == expected


def test_3():
    customers = "YYYY"
    expected = 4
    assert Solution().bestClosingTime(customers) == expected