"""
LeetCode :: July 2021 Challenge :: Three Equal Parts
jramaswami
"""


from collections import defaultdict


class Solution():
    def threeEqualParts(self, bits):

        # We will need the total number of one bits to verify they are
        # divisible by three.
        one_bits = 0
        # We will use suffix totals of one to find out where the second
        # partition point can be.
        suffix_location = defaultdict(list)
        curr_suffix = 0
        # We will use the msb to determine where to start each partition's
        # actual number.
        msb = [0 for _ in bits]
        # We loop backward to compute the total number of one bits, the suffix
        # locations and the msb for each location.
        for i in range(len(bits) - 1, -1, -1):
            curr_suffix += bits[i]
            suffix_location[curr_suffix].append(i)
            one_bits += bits[i]
            if bits[i]:
                msb[i] = i
            else:
                msb[i] = 0 if i + 1 >= len(bits) else msb[i+1]

        # The numbers will have to have the same number of one bits.  If the
        # total number of one bits is not divisible by 3, they cannot be
        # evenly divided in to the three parts.
        if one_bits % 3:
            return [-1, -1]

        current_prefix = 0
        for i, b in enumerate(bits):
            current_prefix += b
            for j in suffix_location[current_prefix]:
                if j <= i:
                    break
                # This may not be the fastest way to do this but its easy.
                left = bits[msb[0]:i+1]
                mid = bits[msb[i+1]:j]
                right = bits[msb[j]:]
                print(left, right, mid)
                if left == mid and mid == right:
                    return [i, j]
        return [-1, -1]


def test_1():
    arr = [1,0,1,0,1]
    left, right = Solution().threeEqualParts(arr)
    assert [left, right] == [0, 3]


def test_2():
    arr = [1,1,0,1,1]
    left, right = Solution().threeEqualParts(arr)
    assert [left, right] == [-1, -1]


def test_3():
    arr = [1,1,0,0,1]
    left, right = Solution().threeEqualParts(arr)
    assert [left, right] == [0, 2]


def test_4():
    """WA"""
    arr = [0,0,0,0,0]
    left, right = Solution().threeEqualParts(arr)
    assert [left, right] == [0, 4]
