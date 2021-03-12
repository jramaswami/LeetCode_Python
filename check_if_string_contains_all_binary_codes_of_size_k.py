"""
LeetCode :: March 2021 Challenge :: Check If a String Contains All Binary Codes of Size K
jramaswami
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        for start, _ in enumerate(s):
            if start + k <= len(s):
                n = int(s[start:start+k], 2)
                codes.add(n)
        return len(codes) == pow(2, k)

def test_1():
    assert Solution().hasAllCodes("00110", 2) == True
    
def test_2():
    assert Solution().hasAllCodes("0110", 1) == True

def test_3():
    assert Solution().hasAllCodes("0110", 2) == False

def test_4():
    assert Solution().hasAllCodes("0000000001011100", 4) == False
