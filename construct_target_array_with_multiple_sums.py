"""
Leet Code :: May 2021 Challenge :: Construct Target Array With Multiple Sums
jramaswami

Thank you Larry!
"""
from typing import *
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        pq = [-n for n in target]
        total = sum(target)
        N = len(target)
        heapq.heapify(pq)
        while pq[0] < -1:
            largest = -heapq.heappop(pq)
            if largest == total:
                return False

            if total - largest == 1:
                return True

            newest = total % (total - largest)
            if newest >= largest:
                return False
            if newest <= 0:
                return False

            total = total - largest + newest
            heapq.heappush(pq, -newest)

        return total == N


def test_1():
    target = [9,3,5]
    assert Solution().isPossible(target) == True


def test_2():
    target = [1,1,1,2]
    assert Solution().isPossible(target) == False


def test_3():
    target = [8,5]
    assert Solution().isPossible(target) == True


def test_4():
    target = [1, 114745, 63211, 225, 229377, 1, 51185]
    assert Solution().isPossible(target) == False


def test_5():
    target = [1081, 1921, 560641, 3841, 1, 1, 30721, 1, 122881, 241, 261121, 1, 541, 31, 1]
    assert Solution().isPossible(target) == False


def test_6():
    target = [26077, 15097, 2361, 8153, 161]
    assert Solution().isPossible(target) == True


def test_7():
    target = [1, 212241, 26545, 3445, 435, 869, 6665, 1, 1737, 1, 13273, 106177, 1, 53089, 1]
    assert Solution().isPossible(target) == True


def test_8():
    """TLE"""
    target = [1,1000000000]
    assert Solution().isPossible(target) == True

#
# Random test generation
#
import random


def random_possible_target(N):
    """Generate a target that is possible."""
    A = [1] * N
    S = N
    for _ in range(15):
        print(A, S)
        i = random.randint(0, len(A)-1)
        A[i] = S
        S = sum(A)
    print(A, S)
    return A


def main():
    # random_possible_target(15)
    target = [1,1,1,2]
    assert Solution().isPossible(target) == True


if __name__ == '__main__':
    main()