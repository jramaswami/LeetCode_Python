"""
LeetCode :: August 2021 Challenge :: Group Anagrams
jramaswami
"""


import collections


class Solution:
    def groupAnagrams(self, strs):
        # Easiest but not the fastest way.
        groups = collections.defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            groups[k].append(s)
        return list(groups.values())


def test_1():
    strs = ["eat","tea","tan","ate","nat","bat"]
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    result = Solution().groupAnagrams(strs)
    print(result)
    assert result == expected
