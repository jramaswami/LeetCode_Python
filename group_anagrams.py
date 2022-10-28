"""
LeetCode :: October 2022 Challenge :: Group Anagrams
jramaswami
"""


class Solution:
    def groupAnagrams(self, strs):
        words = [("".join(sorted(s)), s) for s in strs]
        words.sort()
        soln = []
        curr_group = words[0][0]
        curr_list = []
        for an, wd in words:
            if an == curr_group:
                curr_list.append(wd)
            else:
                soln.append(curr_list)
                curr_list = [wd]
                curr_group = an
        soln.append(curr_list)
        return soln


#
# TESTING
#


def lists_same(A, B):
    # Sort all internal lists.
    for a in A:
        a.sort()
    for b in B:
        b.sort()
    for  a, b in zip(sorted(A), sorted(B)):
        if a != b:
            return False
    return True

def test_1():
    strs = ["eat","tea","tan","ate","nat","bat"]
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    result = Solution().groupAnagrams(strs)
    assert lists_same(expected, result)
