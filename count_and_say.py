"""
LeetCode :: October 2022 Challenge :: 38. Count and Say
jramaswami
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        prev_soln = "1"
        for i in range(1, n):
            curr_soln = []
            curr_num = prev_soln[0]
            curr_freq = 1
            for c in prev_soln[1:]:
                if c == curr_num:
                    curr_freq += 1
                else:
                    curr_soln.append(str(curr_freq))
                    curr_soln.append(curr_num)
                    curr_num = c
                    curr_freq = 1
            curr_soln.append(str(curr_freq))
            curr_soln.append(curr_num)
            prev_soln = "".join(curr_soln)
        return prev_soln


def test_1():
    n = 1
    expected = "1"
    assert Solution().countAndSay(n) == expected


def test_4():
    n = 4
    expected = "1211"
    assert Solution().countAndSay(n) == expected