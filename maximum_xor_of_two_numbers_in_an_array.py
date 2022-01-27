"""
LeetCode :: January 2022 Challenge :: 421. Maximum XOR of Two Numbers in an Array
jramaswami

Thank You Larry!
"""



class TrieNode:
    def __init__(self):
        # There will only be a zero and a one.
        self.one = None
        self.zero = None

    def add_zero(self):
        self.zero = TrieNode()

    def add_one(self):
        self.one = TrieNode()

    def __repr__(self):
        return f"(1:{self.one} 0:{self.zero})"


class Solution:
    def findMaximumXOR(self, nums):
        # Build Trie
        root = TrieNode()
        for n in nums:
            curr = root
            for bit in range(32, -1, -1):
                mask = 1 << bit
                if n & mask:
                    if curr.one is None:
                        curr.add_one()
                    curr = curr.one
                else:
                    if curr.zero is None:
                        curr.add_zero()
                    curr = curr.zero

        # Find max.
        soln = 0
        for n in nums:
            m = 0
            curr = root
            for bit in range(32, -1, -1):
                mask = 1 << bit
                if n & mask:
                    if curr.zero is None:
                        curr = curr.one
                        m |= mask
                    else:
                        curr = curr.zero
                else:
                    if curr.one is None:
                        curr = curr.zero
                    else:
                        curr = curr.one
                        m |= mask
            soln = max(soln, n ^ m)
        return soln



def test_1():
    nums = [3,10,5,25,2,8]
    expected = 28
    assert Solution().findMaximumXOR(nums) == expected


def test_2():
    nums = [14,70,53,83,49,91,36,80,92,51,66,70]
    expected = 127
    assert Solution().findMaximumXOR(nums) == expected


def test_3():
    nums = [8]
    expected = 0
    assert Solution().findMaximumXOR(nums) == expected
