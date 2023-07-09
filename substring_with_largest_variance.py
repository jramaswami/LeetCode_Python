"""
LeetCode
2272. Substring With Largest Variance
July 2023 Challenge
jramaswami
"""


import collections
import itertools


class Solution:
    def largestVariance(self, s: str) -> int:
        soln = 0
        t = set(s)
        for a in t:
            for b in t:
                if a == b:
                    continue
                # print(f"+{a}, -{b}")
                window = collections.deque()
                a_freq = 0
                b_freq = 0
                for char in s:
                    if char == a:
                        a_freq += 1
                        window.append(char)
                    elif char == b:
                        b_freq += 1
                        window.append(char)
                    while b_freq > 1 and a_freq and (b_freq > a_freq):
                        if window[0] == a:
                            a_freq -= 1
                        else:
                            b_freq -= 1
                        window.popleft()
                    if a_freq and b_freq:
                        soln = max(soln, a_freq - b_freq)
                    # print(window)
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


def test_4():
    "WA"
    s = "ykudzhiixwttnvtesiwnbcjmsydidttiyabbwzlfbmmycwjgzwhbtvtxyvkkjgfehaypiygpstkhakfasiloaveqzcywsiujvixcdnxpvvtobxgroznswwwipypwmdhldsoswrzyqthaqlbwragjrqwjxgmftjxqugoonxadazeoxalmccfeyqtmoxwbnphxih"
    expected = 12
    assert Solution().largestVariance(s) == expected
