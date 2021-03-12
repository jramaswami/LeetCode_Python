"""
LeetCode :: March 2021 Challenge :: Check If a String Contains All Binary Codes of Size K
jramaswami
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        limit = pow(2, k)
        has_code = [False for _ in range(limit)]
        # Initialize number to digit length k - 1
        n = 0
        if k > 1:
            n = int(s[:k-1], 2)

        for end, val in enumerate(s):
            if end >= k-1:
                # Shift binary digits one place to the left.
                n <<= 1
                # Add the the last digit.
                n += int(val)
                # Drop the right most bit, if it is set.
                n %= limit
                print(bin(n), end)
                # Remember this number.
                has_code[n] = True

        return all(has_code)


def test_1():
    assert Solution().hasAllCodes("00110", 2) == True
    
def test_2():
    assert Solution().hasAllCodes("0110", 1) == True

def test_3():
    assert Solution().hasAllCodes("0110", 2) == False

def test_4():
    assert Solution().hasAllCodes("0000000001011100", 4) == False
