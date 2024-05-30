"""
LeetCode
1442. Count Triplets That Can Form Two Arrays of Equal XOR
May 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor_prefix = []
        curr_prefix = 0
        for x in arr:
            curr_prefix = curr_prefix ^ x
            xor_prefix.append(curr_prefix)

        def get_xor(left, right):
            if right == -1:
                return 0

            if left == 0:
                return xor_prefix[right]

            if left >= len(arr):
                return 0

            return xor_prefix[left-1] ^ xor_prefix[right]

        soln = 0
        for i, _ in enumerate(arr):
            for j, _ in enumerate(arr[i+1:], start=i+1):
                for k, _ in enumerate(arr[j:], start=j):
                    b = get_xor(i, j-1)
                    c = get_xor(j, k)
                    if b == c:
                        soln += 1
        return soln



def test_1():
    arr = [2,3,1,6,7]
    expected = 4
    assert Solution().countTriplets(arr) == expected


def xtest_2():
    arr = [1,1,1,1,1]
    expected = 10
    assert Solution().countTriplets(arr) == expected