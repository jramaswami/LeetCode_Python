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
        freqs = collections.Counter(s)
        soln = 0

        for a, b in itertools.permutations(freqs, 2):

            freq_a = freqs[a]
            freq_b = freqs[b]

            seen_a = seen_b = False
            delta = 0
            
            for char in s:
                if delta < 0:
                    # If we are negative and there are no more a's left
                    # we can stop looking
                    if freq_a == 0:
                        break

                    # If there are no b's left, we can just take the
                    # remaining b's
                    elif freq_b == 0:
                            soln = max(soln, (delta + freq_a))
                            break

                    # Otherwise, just discard the previous substring
                    else:
                        seen_a = seen_b = False
                        delta = 0
                else:

                    if char == a:
                        delta += 1
                        freq_a -= 1
                        seen_a = True

                    elif char == b:
                        delta -= 1
                        freq_a += 1
                        seen_b = True
                    
                    if seen_a and seen_b:
                        soln = max(soln, delta)
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
