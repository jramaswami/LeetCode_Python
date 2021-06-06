"""
LeetCode :: June 2021 Challenge :: Longest Consecutive Sequence
jramaswami
"""


from typing import *
from collections import namedtuple


EndPoint = namedtuple('EndPoint', ['other', 'length'])


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        endpoints = dict()
        soln = 0
        for n in set(nums):
            before = n - 1 in endpoints
            after = n + 1 in endpoints

            if before and after:
                length = 1 + endpoints[n - 1].length + endpoints[n + 1].length
                soln = max(soln, length)
                left_endpoint = EndPoint(endpoints[n + 1].other, length)
                right_endpont = EndPoint(endpoints[n - 1].other, length)
                endpoints[right_endpoint.other] = left_endpoint
                endpoints[left_endpoint.other] = right_endpoint
            elif before:
                length = 1 + endpoints[n - 1].length
                soln = max(soln, length)
                left_endpoint = EndPoint(endpoints[n - 1].other, length)
                right_endpoint = EndPoint(n, length)
                endpoints[right_endpoint.other] = left_endpoint
                endpoints[left_endpoint.other] = right_endpoint
            elif after:
                length = 1 + endpoints[n + 1].length
                soln = max(soln, length)
                left_endpoint = EndPoint(endpoints[n + 1].other, length)
                right_endpoint = EndPoint(n, length)
                endpoints[right_endpoint.other] = left_endpoint
                endpoints[left_endpoint.other] = right_endpoint
            else:
                length = 1
                soln = max(soln, length)
                endpoints[n] = EndPoint(n, length)

        return soln


def test_1():
    nums = [100,4,200,1,3,2]
    assert Solution().longestConsecutive(nums) == 4


def test_2():
    nums = [0,3,7,2,5,8,4,6,0,1]
    assert Solution().longestConsecutive(nums) == 9


def test_3():
    """WA"""
    nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
    assert Solution().longestConsecutive(nums) == 4
