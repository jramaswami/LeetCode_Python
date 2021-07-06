"""
LeetCode :: July 2021 Challenge :: Reduce Array Size to The Half
jramaswami
"""


from collections import Counter


class Solution:
    def minSetSize(self, arr):
        # Counter to compute frequency of each number in array.
        ctr = Counter(arr)
        N = len(arr)
        soln = 0
        # Sort the frequencies in ascending order, using as a stack.
        freqs = sorted(ctr.values())
        # While there are still more the N / 2 values left ...
        while N * 2 > len(arr):
            # ... remove the number with the highest frequency from the array.
            soln += 1
            # Subtract the frequency removed from the running count, N.
            N -= freqs[-1]
            # Remove the frequency from the list of frequencies.
            freqs.pop()
        return soln


def test_1():
    arr = [3,3,3,3,5,5,5,2,2,7]
    expected = 2
    assert Solution().minSetSize(arr) == expected


def test_2():
    arr = [7,7,7,7,7,7]
    expected = 1
    assert Solution().minSetSize(arr) == expected


def test_3():
    arr = [1,9]
    expected = 1
    assert Solution().minSetSize(arr) == expected



def test_4():
    arr = [1000,1000,3,7]
    expected = 1
    assert Solution().minSetSize(arr) == expected


def test_5():
    arr = [1,2,3,4,5,6,7,8,9,10]
    expected = 5
    assert Solution().minSetSize(arr) == expected


def test_6():
    arr = []
    expected = 0
    assert Solution().minSetSize(arr) == expected
