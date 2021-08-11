"""
LeetCode :: August 2021 Challenge :: Array of Doubled Pairs
jramaswami
"""


import collections


class Solution:
    def canReorderDoubled(self, arr):
        N = len(arr) // 2
        freqs = collections.Counter(arr)
        nums = sorted(arr, key=lambda x: abs(x), reverse=True)
        arr0 = [None for _ in arr]
        for i in range(N):
            # Get rid of any numbers that are unusable.
            while freqs[nums[-1]] <= 0:
                nums.pop()

            # Fill
            a = nums.pop()
            if freqs[a] > 0:
                freqs[a] -= 1
                arr0[i*2] = a
                b = 2 * a
                if freqs[b] > 0:
                    arr0[(i*2)+1] = a
                    freqs[b] -= 1
                else:
                    return False
            else:
                return False
        return True


def test_1():
    arr = [3,1,3,6]
    assert Solution().canReorderDoubled(arr) == False


def test_2():
    arr = [2,1,2,6]
    assert Solution().canReorderDoubled(arr) == False


def test_3():
    arr = [4,-2,2,-4]
    assert Solution().canReorderDoubled(arr) == True


def test_4():
    arr = [1,2,4,16,8,4]
    assert Solution().canReorderDoubled(arr) == False


def test_5():
    arr = []
    assert Solution().canReorderDoubled(arr) == True


def test_5():
    arr = [1,2,4,8,16,32] * 2
    assert Solution().canReorderDoubled(arr) == True


def test_6():
    """WA"""
    arr = [-33,0]
    assert Solution().canReorderDoubled(arr) == False
