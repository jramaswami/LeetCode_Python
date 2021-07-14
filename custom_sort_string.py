"""
LeetCode :: July 2021 Challenge :: Custom Sort String
jramaswami
"""


from collections import Counter


class Solution():
    def customSortString(self, O, T):
        freq_T = Counter(T)
        T0 = []
        for c in O:
            T0.append(c * freq_T[c])
            freq_T[c] = 0
        for c, f in freq_T.items():
            if f:
                T0.append(c * f)
        return "".join(T0)


def test_1():
    order = "cba"
    str = "abcd"
    assert Solution().customSortString(order, str) == "cbad"
