"""
LeetCode
632. Smallest Range Covering Elements from K Lists
October 2024 Challenge
jramaswami
"""


import collections
from typing import List


Item = collections.namedtuple('Item', ['value', 'list_index'])


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        freqs = collections.defaultdict(int)
        uniques = 0

        all_items = []
        for i, NS in enumerate(nums):
            all_items.extend(Item(n, i) for n in NS)

        all_items.sort()

        window = collections.deque()
        # Intitialize
        i = 0
        while i < len(all_items) and uniques < len(nums):
            item = all_items[i]
            i += 1
            window.append(item)
            if freqs[item.list_index] == 0:
                uniques += 1
            freqs[item.list_index] += 1

        soln = [window[0].value, window[-1].value]
        min_range = window[-1].value - window[0].value

        # Sliding window
        while i < len(all_items):
            # Pop leftmost item
            removed_item = window.popleft()
            freqs[removed_item.list_index] -= 1
            if freqs[removed_item.list_index] == 0:
                uniques -= 1

            while uniques < len(nums) and i < len(all_items):
                # Add to window until we have items from every list again
                added_item = all_items[i]
                i += 1
                window.append(added_item)
                if freqs[added_item.list_index] == 0:
                    uniques += 1
                freqs[added_item.list_index] += 1

            if uniques == len(nums):
                curr_range = window[-1].value - window[0].value
                if curr_range < min_range:
                    soln = [window[0].value, window[-1].value]
                    min_range = window[-1].value - window[0].value

        # We have exhaused all the items. Keep doing the sliding
        # window until we no longer have an item from every list.
        while uniques == len(nums):
            # Pop leftmost item
            removed_item = window.popleft()
            freqs[removed_item.list_index] -= 1
            if freqs[removed_item.list_index] == 0:
                uniques -= 1

            if uniques == len(nums):
                curr_range = window[-1].value - window[0].value
                if curr_range < min_range:
                    soln = [window[0].value, window[-1].value]
                    min_range = window[-1].value - window[0].value

        return soln


def test_1():
    nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    expected = [20,24]
    assert Solution().smallestRange(nums) == expected


def test_2():
    nums = [[1,2,3],[1,2,3],[1,2,3]]
    expected = [1,1]
    assert Solution().smallestRange(nums) == expected


def test_3():
    "WA"
    nums = [[10,10],[11,11]]
    expected = [10,11]
    assert Solution().smallestRange(nums) == expected


def test_4():
    "WA"
    nums = [[1,3,5,7,9,10],[2,4,6,8,10]]
    expected = [10,10]
    assert Solution().smallestRange(nums) == expected