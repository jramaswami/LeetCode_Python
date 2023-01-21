"""
LeetCode
93. Restore IP Addresses
January 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        soln = []

        def valid_part(part):
            "Return true if part is valid."
            # No leading zeros.
            if part[0] == '0':
                return len(part) == 1
            return int(part) <= 255

        for a in range(1, min(len(s), 4)):
            if not valid_part(s[:a]):
                break
            for b in range(a+1, min(len(s), a+4)):
                if not valid_part(s[a:b]):
                    break
                for c in range(b+1, min(len(s), b+4)):
                    if valid_part(s[b:c]) and valid_part(s[c:]):
                        ip_addr = ".".join((s[:a], s[a:b], s[b:c], s[c:]))
                        soln.append(ip_addr)
        return soln


def test_1():
    s = "25525511135"
    expected = ["255.255.11.135","255.255.111.35"]
    assert sorted(Solution().restoreIpAddresses(s)) == sorted(expected)


def test_2():
    s = "0000"
    expected = ["0.0.0.0"]
    assert sorted(Solution().restoreIpAddresses(s)) == sorted(expected)


def test_3():
    s = "101023"
    expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    assert sorted(Solution().restoreIpAddresses(s)) == sorted(expected)


def test_4():
    s = '111111111111'
    expected = ['111.111.111.111']
    assert sorted(Solution().restoreIpAddresses(s)) == sorted(expected)