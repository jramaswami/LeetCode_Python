"""
LeetCode :: September 2021 Challenge :: Maximum Length of a Concatenated String with Unique Characters
jramaswami
"""


from collections import namedtuple


Word = namedtuple('Word', ['chars', 'length'])


class Solution:

    def maxLength(self, arr):

        def combine(bitmask, words):
            """
            Combine the words based on the bitmask.  If there is any overlap
            return 0.  If there is no overlap return length of combined word.
            """
            T = set()
            result = 0
            for i in range(len(words)):
                bit = 1 << i
                if bit & bitmask:
                    if not T.isdisjoint(words[i].chars):
                        return 0
                    T.update(words[i].chars)
                    result += words[i].length
            return result

        soln = 0
        words = [Word(set(word), len(word)) for word in arr if len(set(word)) == len(word)]
        for bitmask in range(1, pow(2, len(words))):
            result = combine(bitmask, words)
            soln = max(soln, result)
        return soln



def test_1():
    arr = ["un","iq","ue"]
    expected = 4
    assert Solution().maxLength(arr) == expected


def test_2():
    arr = ["cha","r","act","ers"]
    expected = 6
    assert Solution().maxLength(arr) == expected


def test_3():
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    expected = 26
    assert Solution().maxLength(arr) == expected


def test_4():
    arr = []
    for c in 'abcdefghijklmnop':
        arr.append(c * 26)
    expected = 0
    assert Solution().maxLength(arr) == expected


def test_5():
    """WA"""
    arr = ["yy","bkhwmpbiisbldzknpm"]
    expected = 0
    assert Solution().maxLength(arr) == expected
