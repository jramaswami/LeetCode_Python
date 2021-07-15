"""
LeetCode :: July 2021 Challenge :: Valid Triangle Number
jramaswami
"""


class Solution():
    def triangleNumber(self, nums):
        def binsearch(lo, k):
            hi = len(nums) - 1
            result = lo-1
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if nums[mid] < k:
                    result = max(mid, result)
                    lo = mid + 1
                else:
                    hi = mid - 1
            return result

        soln = 0
        nums.sort()
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                t = binsearch(j+1, a+b)
                # soln += len(nums[j+1:t+1])
                soln += t - j
        return soln


def test_1():
    nums = [2,2,3,4]
    assert Solution().triangleNumber(nums) == 3


def test_2():
    nums = [4,2,3,4]
    assert Solution().triangleNumber(nums) == 4


def test_random():
    from itertools import combinations
    from random import randint
    # Brute force
    def bf(nums):
        expected = 0
        for a, b, c in combinations(nums, 3):
            if a + b > c and a + c > b and b + c > a:
                print("ok", a, b, c)
                expected += 1
        return expected

    for _ in range(10):
        nums = [randint(1, 1000) for _ in range(100)]
        print(nums)
        expected = bf(nums)
        assert expected == Solution().triangleNumber(nums)


def main():
    """Main program to check timing."""
    from random import randint
    nums = [randint(1, 1000) for _ in range(1000)]
    print(nums)
    print(Solution().triangleNumber(nums))


if __name__ == "__main__":
    main()

