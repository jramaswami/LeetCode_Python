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
        for a, b in itertools.permutations(set(s), 2):
            window = collections.deque()
            a_freq = b_freq = 0
            for char in s:
                if char not in (a, b):
                    continue

                window.append(char)
                if char == b:
                    b_freq += 1
                else:
                    a_freq += 1

                # If there are any b's on the tail that we don't need,
                # get rid of them.
                while b_freq > 1 and a_freq > 0 and window[0] == b:
                    window.popleft()
                    b_freq -= 1

                # If the score is negative, discard all but this element
                if b_freq > a_freq:
                    window = collections.deque([char])
                    a_freq, b_freq = 0, 1

                if a_freq and b_freq:
                    soln = max(soln, a_freq - b_freq)
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



def test_5():
    "WA"
    s = "lripaa"
    expected = 1
    assert Solution().largestVariance(s) == expected
