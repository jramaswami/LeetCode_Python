"""
LeetCode :: March 2022 Challenge :: 763. Partition Labels
jramaswami
"""


import collections
import math
import string


class Solution:
    def partitionLabels(self, S):
        min_index = collections.defaultdict(lambda: math.inf)
        max_index = collections.defaultdict(lambda: -math.inf)
        for i, c in enumerate(S):
            min_index[c] = min(min_index[c], i)
            max_index[c] = max(max_index[c], i)

        intervals = []
        for c in string.ascii_lowercase:
            if c in min_index:
                intervals.append((min_index[c], max_index[c]))
        intervals.sort()

        partitions = []
        curr_min = intervals[0][0]
        curr_max = intervals[0][1]
        for mn, mx in intervals[1:]:
            if mn > curr_max:
                partitions.append((curr_min, curr_max))
                curr_min = mn
            curr_max = max(mx, curr_max)
        partitions.append((curr_min, curr_max))
        return [mx - mn + 1 for mn, mx in partitions]



def test_1():
    s = "ababcbacadefegdehijhklij"
    expected = [9,7,8]
    assert Solution().partitionLabels(s) == expected


def test_2():
    s = "eccbbbbdec"
    expected = [10]
    assert Solution().partitionLabels(s) == expected
