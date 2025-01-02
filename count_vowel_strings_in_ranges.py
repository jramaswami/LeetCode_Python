"""
LeetCode
2559. Count Vowel Strings in Ranges
January 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(c):
            return c in 'aeiou'

        # Prefix sums for number of words starting/ending with vowel
        prefix_sums = []
        curr_count = 0
        for wd in words:
            if is_vowel(wd[0]) and is_vowel(wd[-1]):
                curr_count += 1
            prefix_sums.append(curr_count)

        def get(left, right):
            if left == 0:
                return prefix_sums[right]
            return prefix_sums[right] - prefix_sums[left-1]
        
        return [get(l, r) for l, r in queries]



def test1():
    words = ["aba","bcb","ece","aa","e"]
    queries = [[0,2],[1,4],[1,1]]
    expected = [2,3,0]
    assert Solution().vowelStrings(words, queries) == expected


def test2():
    words = ["a","e","i"]
    queries = [[0,2],[0,1],[2,2]]
    expected = [3,2,1]
    assert Solution().vowelStrings(words, queries) == expected
