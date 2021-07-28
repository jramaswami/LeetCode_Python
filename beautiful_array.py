"""
LeetCode :: July 2021 Challenge :: Beautiful Array
jramaswami

For some fixed n, an array nums is beautiful if it is a permutation of the
integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that
nums[k] * 2 = nums[i] + nums[j].

Thank You Larry!
"""


class Solution:
    def beautifulArray(self, n):

        def reverse_bits(k):
            """Return the reversed bitstring for k."""
            return bin(k)[2:][::-1]

        return sorted(list(range(1, n + 1)), key=lambda k: reverse_bits(k))


def valid(nums):
    for i, _ in enumerate(nums):
        nums_left = set()
        nums_left.add(nums[i])
        for j, _ in enumerate(nums[i+1:], start=i+1):
            s = nums[i] + nums[j]
            if s % 2 == 0 and s // 2 in nums_left:
                print(f"{nums[i]=} + {nums[j]} = {s} and {s // 2} is in {nums[i:j+1]}")
                return False
            nums_left.add(nums[j])
    return True


def test_1():
    assert valid(Solution().beautifulArray(4))


def test_2():
    assert valid(Solution().beautifulArray(5))


def test_3():
    assert valid(Solution().beautifulArray(1000))


def test_all():
    for n in range(1, 1001):
        assert valid(Solution().beautifulArray(n))


def main():
    """Main program."""
    for n in range(1, 1001):
        oks = 0
        if valid(Solution().beautifulArray(n)):
            oks += 1
            print(n, 'ok')
        else:
            print(n, 'FAIL')
        if oks == 1000:
            print("ALL OK")


if __name__ == '__main__':
    main()
