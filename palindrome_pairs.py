"""
LeetCode :: September 2022 Challenge :: Palindrome Pairs
jramaswami
"""


from typing import *


def is_palindrome(s):
    """Simplest way to test for a palindrome."""
    return s == s[::-1]


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_lookup = {w: i for i, w in enumerate(words)}
        soln = []
        for i, word in enumerate(words):
            # Case 1: word == "": this will allow palindrome for
            # all words that are already palindromes.
            if word == "":
                for word0 in words:
                    if is_palindrome(word0):
                        j = words_lookup[word0]
                        if i != j:
                            soln.append([i, j])
                            soln.append([j, i])

            # Case 2: word + word[::-1] is a palindrome.
            rev_word = word[::-1]
            if rev_word in words_lookup:
                j = words_lookup[rev_word]
                if i != j:
                    soln.append([i, words_lookup[rev_word]])

            for cut in range(1, len(word)):
                left = word[:cut]
                right = word[cut:]
                rev_left = left[::-1]
                rev_right = right[::-1]

                # Case 3: if left is a palindrome and rev_right is in words,
                # then rev_right + word is a palindrome.
                if is_palindrome(left):
                    if rev_right in words_lookup:
                        j = words_lookup[rev_right]
                        if i != j:
                            soln.append([j, i])

                # Case 4: if right is a palindrome and rev_left is in words,
                # then word + rev_right is a palindrome.
                if is_palindrome(right):
                    if rev_left in words_lookup:
                        j = words_lookup[rev_left]
                        if i != j:
                            soln.append([i, j])

        return soln


def test_1():
    words = ["abcd","dcba","lls","s","sssll"]
    expected = sorted([[0,1],[1,0],[3,2],[2,4]])
    assert sorted(Solution().palindromePairs(words)) == expected


def test_2():
    words = ["bat","tab","cat"]
    expected = sorted([[0,1],[1,0]])
    assert sorted(Solution().palindromePairs(words)) == expected


def test_3():
    words = ["a",""]
    expected = sorted([[0,1],[1,0]])
    assert sorted(Solution().palindromePairs(words)) == expected


def test_4():
    words = []
    with open('palindrome_pairs_test4.txt', 'r') as testin:
        for line in testin:
            words.append(line.strip())
    expected = sorted([[7,47],[229,7],[10,71],[11,466],[159,11],[20,15],[16,250],[250,16],[159,22],[38,229],[250,38],[632,40],[44,111],[159,44],[44,531],[65,39],[307,65],[673,73],[73,584],[229,73],[366,75],[29,86],[94,111],[584,94],[115,159],[229,115],[115,263],[133,29],[29,133],[466,142],[152,38],[169,229],[520,169],[175,71],[159,175],[176,39],[466,176],[184,250],[47,184],[184,308],[188,47],[214,71],[229,214],[214,673],[230,29],[250,230],[230,525],[232,307],[236,327],[240,307],[250,240],[240,327],[466,244],[263,229],[159,263],[263,115],[273,111],[47,273],[279,250],[39,279],[250,281],[308,47],[250,308],[308,184],[327,250],[307,327],[327,240],[342,466],[348,307],[229,348],[350,250],[350,240],[361,71],[47,361],[366,111],[466,366],[366,410],[374,466],[29,374],[376,133],[229,376],[184,382],[403,466],[466,403],[410,466],[111,410],[410,366],[423,47],[29,423],[440,39],[29,440],[441,229],[159,441],[445,159],[452,525],[459,115],[7,482],[47,505],[520,279],[525,250],[29,525],[525,230],[531,159],[111,531],[531,44],[539,29],[111,539],[185,545],[584,71],[71,584],[609,230],[632,361],[641,734],[29,643],[667,673],[71,669],[673,229],[71,673],[673,214],[683,47],[263,686],[706,250],[327,708],[708,240],[734,641],[736,374],[115,760],[764,39],[133,764]])
    assert sorted(Solution().palindromePairs(words)) == expected
