"""
LeetCode
1601. Maximum Number of Achievable Transfer Requests
July 2023 Challenge
jramaswami
"""

from maximum_number_of_achievable_transfer_requests import Solution


def test_1():
    n = 5
    requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    expected = 5
    assert Solution().maximumRequests(n, requests) == expected


def test_2():
    n = 3
    requests = [[0,0],[1,2],[2,1]]
    expected = 3
    assert Solution().maximumRequests(n, requests) == expected


def test_3():
    n = 4
    requests = [[0,3],[3,1],[1,2],[2,0]]
    expected = 4
    assert Solution().maximumRequests(n, requests) == expected


def test_4():
    "TLE"
    n = 2
    requests = [[1,0],[0,0],[1,0],[0,1],[0,1],[1,1],[0,1],[0,0],[0,0],[0,1],[1,0],[0,0],[0,1],[1,1],[1,1]]
    expected = -1
    assert Solution().maximumRequests(n, requests) == expected