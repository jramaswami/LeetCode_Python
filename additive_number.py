"""
LeetCode :: 306. Additive Number
jramaswami
"""


class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        # Boundary case: not enough string.
        if len(num) < 3:
            return False
        # Boundary case: two leading zeros.
        if num[:2] == '00':
            return all(c == '0' for c in num)

        # Pick any two starting numbers.
        for i, _ in enumerate(num):
            a = int(num[:i+1])
            for j, _ in enumerate(num[i+1:], start=i+1):
                b = int(num[i+1:j+1])
                stack = [a, b]
                k = j+1
                while k < len(num):
                    t = str(sum(stack[-2:]))
                    if num[k:].startswith(t):
                        stack.append(sum(stack[-2:]))
                        k += len(t)
                    else:
                        stack = []
                        k = len(num)
                if len(stack) > 2:
                    # print(stack)
                    return True
                if b == 0:
                    # If b is zero we cannot make a larger number.
                    break
            if a == 0:
                # If a is zero, then we cannot make a larger number.
                break
        return False

def test_1():
    num = "112358"
    expected = True
    assert Solution().isAdditiveNumber(num) == expected


def test_2():
    num = "199100199"
    expected = True
    assert Solution().isAdditiveNumber(num) == expected


def test_3():
    "RTE"
    num = "0"
    expected = False
    assert Solution().isAdditiveNumber(num) == expected


def test_4():
    "WA"
    num = "111"
    expected = False
    assert Solution().isAdditiveNumber(num) == expected


def test_5():
    "WA"
    num = "101"
    expected = True
    assert Solution().isAdditiveNumber(num) == expected


def test_6():
    num = "000"
    expected = True
    assert Solution().isAdditiveNumber(num) == expected


def test_7():
    num = "0199100199"
    expected = False
    assert Solution().isAdditiveNumber(num) == expected


def test_8():
    "WA"
    num = "1203"
    expected = False
    assert Solution().isAdditiveNumber(num) == expected


# if __name__ == '__main__':
#     test_7()