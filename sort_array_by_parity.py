"""
LeetCode :: Array Module :: Sort Array by Parity
jramaswami
"""

class Solution:
    def sortArrayByParity(self, nums):
        if len(nums) < 2:
            return nums

        # Similar to Hoare Partition
        i = -1
        j = len(nums)
        while 1:
            # Find rightmost item that is odd
            while 1:
                i += 1
                if i >= len(nums) or nums[i] % 2 == 1:
                    break

            # Find left most item that is even
            while 1:
                j -= 1
                if j < 0 or nums[j] % 2 == 0:
                    break

            if i >= j:
                break

            # Swap the two items
            nums[i], nums[j] = nums[j], nums[i]

        return nums


def first_odd(A):
    for i, n in enumerate(A):
        if n % 2:
            return i
    return len(A)


def valid(A):
    p = first_odd(A)
    return all(n % 2 == 0 for n in A[:p]) and all(n % 2 == 1 for n in A[p:])


def test_1():
    nums = [3, 1, 2, 4]
    Solution().sortArrayByParity(nums)
    print(nums)
    assert valid(nums)


def test_random():
    import random
    for _ in range(100):
        N = pow(10, 4)
        A = [random.randint(0, 5000) for _ in range(N)]
        Solution().sortArrayByParity(A)
        print(A)
        assert valid(A)


def test_2():
    """RTE"""
    nums = [0]
    Solution().sortArrayByParity(nums)
    print(nums)
    assert valid(nums)
