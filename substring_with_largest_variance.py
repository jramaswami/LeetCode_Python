"""
LeetCode
2272. Substring With Largest Variance
July 2023 Challenge
jramaswami
"""


class Solution:
    def largestVariance(self, s: str) -> int:
        soln = 0
        for i, a in enumerate(s):
            freqs = [0 for _ in range(26)]
            freqs[ord(a) - ord('a')] += 1
            for b in s[i+1:]:
                freqs[ord(b) - ord('a')] += 1
                soln = max(soln, max(freqs) - min(f for f in freqs if f > 0))
        return soln


def test_1():
    s = "aababbb"
    expected = 3
    assert Solution().largestVariance(s) == expected


def test_2():
    s = "abcde"
    expected = 0
    assert Solution().largestVariance(s) == expected


def test_3():
    "TLE, as expected"
    s = "txcvvetpmlwiignoirbqsykwozgggxkrmanhvkygkvfxwpzsbnfjtxnviocpgsaferjylutkwcfyditouydtcttsxylgszhjpxqikpulomcxyseyjapsmstwtdeycxlmspfuegsjsrphbrrehhvgmwdufzkqsuzjjsbohigaqtvzwosahlsbqkvxqdtebccbtzsskrieeinapzvllnxkwpycfkhfwrdgdjigzqdblmuzhktwtpiysrziylngctnqwwicihdnxvaqpwackcreovdkvjcgmnibtpoeiuwglwncskaktjpmrcupiwrpzjdbpkhmauhowpznssonwfyfmwkgxaqjkxlunpbaleacxgvrlkytxgrqjbypswuscwcmrvwbzwxngnyuvhuzafeqvpvhgjqhkdvtfrteldjcqgrjsrtaxdjnmujjfkjcythfzfwekxfpgzkjdivizbaaedytpwgnueirwesuacqgafczaszsxtzvmqutqekmthwncuyqpkbiwuuoyyzhuiljlacifvisvklgwwaowoecvfzeyzlqltpenuhqntuivbecmcbjjtxotmchudzmskprysyyviedbwcocuebbyhgeeqypvttcrrcqumiydnxwuvbxkaminkppmwflriibsmgnhgpuhfudcuasgvfgwnrnxamolsqvsssltprikladlnronbsiyxjpmvogunhmqdeefweplxdibtblvfxgdhapsuhbaxsoiwtfolqcfanjciewmjmidvomjpgzzyucosovfgmhsezxevxcckaixdvnbbtescizsrkeygkvysorcscocvdwvldspupvnrhnracvoyhntxwzsyjjokaysbclkgynywqgcsxiwwwwhprhzuxagxmufnorsxcpzqnncskjhbmbiyiuvewzpczyymowbuhtwnfpbmkxshuseqnvpbvqprykixeitgxvwaebdgawzjenepjgzcdvdgzwcwfgtqlwpqtmrishdyobavzzzgzuxfokcmmhjqgorovmvrrjsgtgzyqecprskllzcgkzvaleyjybychhiwxeingqoeieuirbibtpaescmnhchtdykrsowvwoogcjwrxjupepdkhzfrcvaykhorghfvfjavowsmjvunkmhsvihmttdjvpajwgplqbkuwohdqptjxxmvoeyjqjdrhmgmudmahdfjrccplccdrkctislwjvwafgrebdqoiewrxdbvrsqgttpsltworsewhvtaqqavapmqdhkybiksqgmgnaottmrjfkqthabrhvfvomobytpnwvotvojnvxndxezlbnchzlqfiqnrubjjrqvauvyhcvoslyaimdmjcaivnvnvorpczkzxnfyccunvjxklfwmnnpxunvcupkqgczyhzrrlmdqmqgcefketuzrhbzqwznlshemjhgoepvdxxjnzgtrsxophoooxjcp"
    expected = 33
    assert Solution().largestVariance(s) == expected

